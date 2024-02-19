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
        self.config = json.load(open(os.path.join(script_dir, './config.json'), 'r'))
        self.path = self.config['prompt_path']
        self.messages = self.config['messages']['prompt']
        self.chat_model = self.config['chat_model']
        dashscope.api_key = self.config["api-key"]

    def set_prompts(self):
        for para in self.story_paragraph:
            self.prompts.append('请你为以下小说文本生成英文提示词：{}'.format(para))

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
            file.writelines('{0}\n{1}\n======\n'.format(self.story_paragraph[index], prompt.replace('"', '')))
        file.close()


if __name__ == "__main__":
    try:
        story = sys.argv[1]
        # story = '在繁华的城市角落，有一个古老的学院——枫叶学院。这里有着浓郁的学习氛围和人文气息，每年都会吸引无数学子前来求学。而在枫叶学院的一角，有这样一对恋人在演绎着属于他们的爱情故事。\n\n男主角林然，他是学院的学霸，不仅学习成绩优异，而且人缘极好，深受师生们的喜爱。他目光坚定，为人谦逊，给人一种内敛而深邃的感觉。\n\n女主角苏梦，则是一个活泼开朗的女生，她笑起来的时候眼睛弯弯的，犹如春日暖阳，总能给周围的人带来正能量。她聪明机智，与林然的性格截然相反，但却能互补对方的不足。\n\n两人的相遇是在一个偶然的机会，在一场公益活动上，林然被苏梦的热情和善良所打动，而苏梦也被林然的稳重和内敛所吸引。从此，两人开始了他们的甜蜜之旅，一起经历了许多难忘的事情。\n\n然而，随着高三的到来，他们的关系也变得更加微妙。林然为了实现自己的梦想，决定全力以赴备战高考，而苏梦则选择默默支持他，成为他背后的那个人。\n\n经过一年的努力，林然成功考上了自己心仪的大学，而苏梦也如愿以偿地进入了一个理想的大学。在毕业典礼上，林然深情地向苏梦表白，希望她能够陪他一起去新的城市，开始新的人生。苏梦感动得热泪盈眶，欣然接受了林然的邀请，他们的故事在这里画下了一个完美的结局。'
        gpp = GeneratePicturePrompt(story)
        gpp.generate()
        gpp.save_prompt()

        print("Over")
    except Exception as e:
        print("Error in GeneratePicturePrompt.py: {}".format(e))
