import sys
import os
import json
import random
from http import HTTPStatus
import dashscope
from dashscope.api_entities.dashscope_response import Role

script_dir = os.path.dirname(os.path.abspath(__file__))


class GenerateStory(object):
    def __init__(self, prompt):
        self.story = ''
        self.path = ''
        self.config = {}
        self.prompt = prompt
        self.messages = []
        self.chat_model = ''  # 采用模型
        self.chat = dashscope.Generation

        self.set_config()

    def set_config(self):
        self.config = json.load(open(os.path.join(script_dir, './config.json'), 'r'))
        self.path = self.config['story_path']
        self.messages = self.config['messages']['story']
        self.chat_model = self.config['chat_model']
        dashscope.api_key = self.config["api-key"]

    def save_config(self):
        json.dump(self.config, open(os.path.join(script_dir, './config.json'), 'w', encoding='utf-8'),
                  ensure_ascii=False)

    def generate(self):
        self.messages.append({
            'role': Role.USER,
            'content': self.prompt
        })

        response = self.chat.call(
            self.chat_model,
            messages=self.messages,
            # 设置一个种子，并不是必要参数
            seed=random.randint(1, 10000),
            result_format='message',
        )

        if response.status_code == HTTPStatus.OK:
            self.story = response.output.choices[0]['message']['content']
            self.messages.append(
                {
                    'role': response.output.choices[0]['message']['role'],
                    'content': self.story
                }
            )
        else:
            raise Exception(response.message)

    def save_story(self):
        file = open(os.path.join(script_dir, self.path), 'w', encoding='utf-8')
        file.writelines(self.story)
        file.close()


if __name__ == "__main__":
    try:
        prompt = sys.argv[1]  # "请你写一篇关于反映农村艰苦生活的短篇小说"
        story = GenerateStory(prompt)
        story.generate()
        story.save_story()
        story.save_config()

        print("Over")
    except Exception as e:
        print("Error in GenerateStory.py: {}".format(e))
