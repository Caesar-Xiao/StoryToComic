<template>
  <div class="Panel" id="LeftPanel">
    <StoryPanel></StoryPanel>
    <PicturePromptPanel></PicturePromptPanel>
  </div>
</template>

<script setup lang="ts" name="LeftPanel">
  import StoryPanel from './StoryPanel.vue';
  import PicturePromptPanel from './PicturePromptPanel.vue';

</script>

<style scoped>
  #LeftPanel {
    width: 25%;
  }
</style>
