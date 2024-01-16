<template>
    <div id="PicturePromptViewport">
    </div>
</template>

<script setup lang="ts" name="PicturePromptViewport">
    import { ref, watch } from 'vue';
    import emitter from '@/utils/Emitter';
    import callPthon from "@/utils/PythonCaller";
    import loadTextFile from "@/utils/LoadTextFile";
    import usePicturePrompt from '@/store/picture_rompt';
    import type { PicturePromptStore } from '@/utils/Types';
    import { ElMessage, ElLoading } from 'element-plus';

    // picture prompt
    const picturePrompt = usePicturePrompt();
    const loadPrompt = () => {
        loadTextFile('load-prompt', (prompts: PicturePromptStore) => {
            Object.assign(picturePrompt, prompts);
            if (picturePrompt.error)
                ElMessage(`提示词读取失败！\n${picturePrompt.error}`);
            console.log(picturePrompt)
        });
    };

    // story
    const story = ref('');

    emitter.on('sharePicturePrompt', (prompt: string) => story.value = prompt);
    watch(story, (value: string) => {
        // const loading = setLoading();
        // showStory.value = true;
        // menuDisabled.value = true;
        emitter.emit('setSendButtonStatus', true);

        callPthon('GeneratePicturePrompt', value,
            (res: string) => {
                if (res === 'Over')
                    loadPrompt();
                else {
                    // showStory.value = false;
                    ElMessage(`提示词生成失败！\n${res}`);
                }

                // loading.close();
                // menuDisabled.value = false;
                emitter.emit('setSendButtonStatus', false);
            });
    });


</script>

<style scoped>
    #PicturePromptViewport {
        width: 100%;
        padding: 10px;
        height: calc(100% - 42px);
    }
</style>