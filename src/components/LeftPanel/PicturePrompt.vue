<template>
    <div class="ChildPanel" id="picturePrompt">
        <PicturePromptViewport></PicturePromptViewport>
        <PromptInput input-type="textarea" prompt-type="Story" placeholder="请输入故事文本"></PromptInput>
    </div>
</template>

<script setup lang="ts" name="PicturePrompt">
    import PromptInput from '../PromptInput.vue';
    import PicturePromptViewport from './PicturePromptViewport.vue';
</script>

<style scoped>
    #picturePrompt {
        height: 50%;
        overflow-x: hidden;
        overflow-y: auto;
    }
</style>