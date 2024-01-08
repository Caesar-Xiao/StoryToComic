<template>
  <div class="Panel" id="LeftPanel">
    <StoryPanel></StoryPanel>
    <PicturePrompt></PicturePrompt>
  </div>
</template>

<script setup lang="ts" name="LeftPanel">
import StoryPanel from './StoryPanel.vue';
import PicturePrompt from './PicturePrompt.vue';

</script>

<style scoped>
  #LeftPanel {
    width: 25%;
  }
</style>
