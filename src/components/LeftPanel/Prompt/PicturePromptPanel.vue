<template>
    <div class="ChildPanel" id="picturePrompt">
        <PicturePromptViewport></PicturePromptViewport>
        <PromptInput input-type="textarea" prompt-type="Picture" :autosize="true" placeholder="请输入故事文本" />
    </div>
</template>

<script setup lang="ts" name="PicturePromptPanel">
    import PromptInput from '@/components/PromptInput.vue';
    import PicturePromptViewport from './PicturePromptViewport.vue';
</script>

<style scoped>
    #picturePrompt {
        height: 50%;
        overflow-x: hidden;
        overflow-y: auto;
    }
</style>