import { defineStore } from "pinia";
import type { PicturePromptType } from "@/utils/Types";

const usePicturePrompt = defineStore("picture_prompt", {
    state() {
        const prompts: PicturePromptType[] = [];

        return {
            error: null,
            prompts
        };
    }
});

export default usePicturePrompt;