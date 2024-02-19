<template>
  <LeftPanel></LeftPanel>
  <MiddelPanel></MiddelPanel>
  <RightPanel></RightPanel>
</template>

<script setup lang="ts" name="App">
  import LeftPanel from "./components/LeftPanel/LeftPanel.vue";
  import MiddelPanel from "./components/MiddlePanel/MiddlePanel.vue";
  import RightPanel from "./components/RightPanel/RightPanel.vue";
</script>

<style>
  .Panel {
    height: 100%;
  }

  .ChildPanel {
    width: 100%;
  }
</style>
