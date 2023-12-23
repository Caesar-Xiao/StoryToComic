"""
coding:utf-8
@Software:PyCharm
@Time:2023/9/12 14:49
@Author:Caesar Xiao
@Introduce: Transfer story to comic
"""
import sys
import random
from http import HTTPStatus
import dashscope
from dashscope.api_entities.dashscope_response import Role
from StableDiffusion import StableDiffusion


class StoryToComic(object):
    def __init__(self, n_steps=20, n_pictures=1):
        self.api_key = "sk-94e7ec7817d3443da33221bd9da2fef2"
        self.messages = [{
            'role': Role.SYSTEM,
            'content': '你现在是知名的短篇小说代写者，现在你需要为客户代写高质量的短篇小说。'
        }]

        self.story = ''
        self.picture_prompt = ''
        self.images = []
        self.error = None

        dashscope.api_key = self.api_key
        self.chat = dashscope.Generation
        self.chat_model = 'qwen-72b-chat'  # 采用模型

        self.base_path = '../../public/result/'
        self.SDXL = StableDiffusion(n_steps=n_steps, n_pictures=n_pictures)

    def generate_story(self, prompt):
        self.messages.append({
            'role': Role.USER,
            'content': prompt
        })

        response = self.chat.call(
                'qwen-72b-chat',
                messages=self.messages,
                # 设置一个种子，并不是必要参数
                seed=random.randint(1, 10000),
                result_format='message',
        )

        self.story = ''
        self.error = None
        if response.status_code == HTTPStatus.OK:
            self.story = response.output.choices[0]['message']['content']
            self.messages.append(
                    {
                        'role': response.output.choices[0]['message']['role'],
                        'content': self.story
                    }
            )
        else:
            self.error = 'Error: '.format(response.message)

        self.save_files("story", self.story, self.error)

    def extract_comic_prompt(self):
        self.messages.append({
            'role': 'user',
            'content': '请你将以上小说的每个段落生成一段Stable Diffusion模型的英文提示词'
        })

        response = self.chat.call(
                self.chat_model,
                messages=self.messages,  # 信息列表
                result_format='message',  # 设置格式为message
        )

        self.error = None
        self.picture_prompt = ''
        if response.status_code == HTTPStatus.OK:
            self.picture_prompt = response.output.choices[0]['message']['content']
        else:
            self.error = response.message

        self.save_files("picture_prompt", self.picture_prompt, self.error)

    def generate_pictures(self):
        self.images = self.SDXL.run(self.picture_prompt)
        for index, image in enumerate(self.images):
            image.save('{0}/images/result_{1}.png'.format(self.base_path, index))

    def save_files(self, path, result, error):
        file = open(self.base_path + path, 'w', encoding='utf-8')
        file.writelines(result if error is None else error)
        file.close()

    def clear_params(self):
        self.messages = []
        self.story = ''
        self.error = None


if __name__ == "__main__":
    prompt = sys.argv[1]  # "请你写一篇关于反映农村艰苦生活的短篇小说"
    transfer = StoryToComic()
    transfer.generate_story(prompt)
    transfer.extract_comic_prompt()
    transfer.clear_params()
    transfer.generate_pictures()
