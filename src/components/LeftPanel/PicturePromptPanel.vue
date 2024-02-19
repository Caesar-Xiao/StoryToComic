<template>
    <div class="ChildPanel" id="picturePromptViewport">
        <Viewport type="Picture-Prompt" info="提示词" :data-store="picturePromptStore">
            <template #default="{ showResult }">
                <div id="picturePrompt" ref="picturePromptDom">
                </div>
            </template>
        </Viewport>
        <PromptInput input-type="textarea" prompt-type="PicturePrompt" :autosize="true" placeholder="请输入故事文本" />
    </div>
</template>

<script setup lang="ts" name="PicturePromptPanel">
    import { ref, provide } from 'vue';
    import Viewport from '@/components/Viewport.vue';
    import PromptInput from '@/components/PromptInput.vue';
    import usePicturePromptStore from '@/store/picture_rompt';

    const picturePromptStore = usePicturePromptStore();
    const picturePromptDom = ref();
    provide('loadingDom', picturePromptDom);
</script>

<style scoped>
    #picturePromptViewport {
        height: 50%;
        overflow-x: hidden;
        overflow-y: auto;
    }

    #picturePrompt {
        width: 100%;
        padding: 10px;
        height: calc(100% - 42px);
    }
</style>