<template>
  <div class="ChildPanel" id="storyPanel">
    <el-text class="w-150px mb-2"> </el-text>
    <ChatViewport></ChatViewport>
    <PromptInput prompt-type="Story" placeholder="请输入故事描述"></PromptInput>
  </div>
</template>

<script setup lang="ts" name="StoryPanel">
  import ChatViewport from './ChatViewport.vue';
  import PromptInput from '../PromptInput.vue';
</script>

<style scoped>
  #storyPanel {
    height: 50%;
    justify-content: center;
    display: flex;
    border-bottom: 1px solid #91acb7;
    flex-direction: column;
  }
</style>