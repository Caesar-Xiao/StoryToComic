from diffusers import DiffusionPipeline
import torch


class StableDiffusion(object):
    def __init__(self, n_steps=20, n_pictures=1, high_noise_frac=0.8):
        self.pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0",
                                                      torch_dtype=torch.float16, variant="fp16", use_safetensors=True)
        self.refiner = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-refiner-1.0",
                                                         text_encoder_2=self.pipe.text_encoder_2, vae=self.pipe.vae,
                                                         torch_dtype=torch.float16, use_safetensors=True,
                                                         variant="fp16")

        self.pipe.to("cuda")
        self.refiner.to("cuda")

        self.n_steps = n_steps
        self.n_pictures = n_pictures
        self.high_noise_frac = high_noise_frac

    def run(self, prompt):
        image = self.pipe(prompt=prompt, num_inference_steps=self.n_steps, num_images_per_prompt=self.n_pictures,
                          denoising_end=self.high_noise_frac,
                          output_type="latent").images

        return self.refiner(prompt=prompt, num_inference_steps=self.n_steps, num_images_per_prompt=self.n_pictures,
                            denoising_start=self.high_noise_frac,
                            image=image).images


if __name__ == '__main__':
    test_prompt = ["A majestic lion jumping from a big stone at night"]
    SDXL = StableDiffusion()
    results = SDXL.run(test_prompt)
    for index, result in enumerate(results):
        result.save('../public/images/result_{0}.png'.format(index))
