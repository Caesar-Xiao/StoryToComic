import sys
import os
import json
import random
from http import HTTPStatus
import dashscope
from dashscope.api_entities.dashscope_response import Role

script_dir = os.path.dirname(os.path.abspath(__file__))


class GeneratePicturePrompt(object):
    def __init__(self, story):
        self.picture_prompts = []
        self.path = ''
        self.config = {}
        self.prompts = []
        self.messages = []
        self.chat_model = ''  # 采用模型
        self.chat = dashscope.Generation
        self.story_paragraph = list(filter(lambda p: p.strip(), story.split('\n')))

        self.set_config()
        self.set_prompts()

    def set_config(self):
        self.config = json.load(open(os.path.join(script_dir, './config.json'), 'r', encoding='utf-8'))
        self.path = self.config['prompt_path']
        self.messages = self.config['messages']['prompt']
        self.chat_model = self.config['chat_model']
        dashscope.api_key = self.config["api-key"]

    def set_prompts(self):
        for para in self.story_paragraph:
            self.prompts.append('请你为以下小说文本生成英文提示词：{}'.format(para.strip()))

    def generate(self):
        for prompt in self.prompts:
            messages = [
                self.messages[0],
                {
                    'role': Role.USER,
                    'content': prompt
                }
            ]

            response = self.chat.call(
                self.chat_model,
                messages=messages,
                # 设置一个种子，并不是必要参数
                seed=random.randint(1, 10000),
                result_format='message',
            )

            if response.status_code == HTTPStatus.OK:
                picture_prompt = response.output.choices[0]['message']['content']
                self.picture_prompts.append(picture_prompt)
                self.messages.append(
                    {
                        'role': response.output.choices[0]['message']['role'],
                        'content': picture_prompt
                    }
                )
            else:
                raise Exception(response.message)

    def save_prompt(self):
        file = open(os.path.join(script_dir, self.path), 'w', encoding='utf-8')
        for index, prompt in enumerate(self.picture_prompts):
            file.writelines('{0}\n{1}\n======\n'.format(self.story_paragraph[index].strip(), prompt.strip().replace('"', '')))
        file.close()


if __name__ == "__main__":
    try:
        story = sys.argv[1]
        gpp = GeneratePicturePrompt(story)
        gpp.generate()
        gpp.save_prompt()

        print("Over")
    except Exception as e:
        print("Error in GeneratePicturePrompt.py: {}".format(e))
