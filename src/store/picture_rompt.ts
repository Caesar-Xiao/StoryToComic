import { defineStore } from "pinia";
import type { PicturePromptType } from "@/utils/Types";

const usePicturePromptStore = defineStore("picture_prompt", {
    state() {
        const prompts: PicturePromptType[] = [];

        return {
            error: null,
            prompts
        };
    }
});

export default usePicturePromptStore;