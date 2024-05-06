import sys
import os
from StableDiffusion import StableDiffusion

script_dir = os.path.dirname(os.path.abspath(__file__))

class GeneratePictures(object):
    def __init__(self, prompts, n_pictures=1):
        self.model = StableDiffusion(n_pictures=n_pictures)
        self.images = []
        self.prompts = prompts
        self.n_pictures = n_pictures
        self.images_folder = os.path.join(script_dir,  '../result/images/')

    def generate(self):
        self.images = self.model.run(self.prompts)

    def save_pictures(self):
        self.clear_images_folder()
        for index, result in enumerate(self.images):
            result.save(f'{self.images_folder}result_{index // self.n_pictures}_{index % self.n_pictures}.png')

    def clear_images_folder(self):
        for filename in os.listdir(self.images_folder):
            file_path = os.path.join(self.images_folder, filename)
            os.unlink(file_path)


if __name__ == '__main__':
    # prompt_list = ["A majestic lion jumping from a big stone at night",
    #                "summer sunlight, shaded campus path, encounter, Lin Xiao, Chen Ran, classmates, Grade 11, introverted, artistic, painting, energetic, outgoing, basketball star, parallel worlds, chance assistance, intersecting paths."]  # sys.argv[1]
    # gp = GeneratePictures(prompt_list)
    # gp.generate()
    # gp.save_pictures()
    try:
        prompt_list = sys.argv[1].split('===')
        pictures_num =1 #int(sys.argv[2])
        gp = GeneratePictures(prompt_list, n_pictures=pictures_num)
        gp.generate()
        gp.save_pictures()

        print("Over")
    except Exception as e:
        print("Error in GeneratePictures.py: {}".format(e))
