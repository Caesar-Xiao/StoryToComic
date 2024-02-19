<template>
  <div class="ChildPanel" id="storyPanel">
    <el-text class="w-150px mb-2"> </el-text>
    <Viewport type="Story" info="故事" :data-store="storyStore" :pre-handler="preHandler" :post-handler="postHandler">
      <template #default="{ prompt, showResult }">
        <div v-show="showResult" class="chat-bubble" id="story" ref="storyDom">
          <div id="title"> {{ storyStore.title }} </div>
          <div id="content">
            <p v-for="para in storyStore.content.split('\n')" class="StoryParagraphs">
              {{ para }}
            </p>
          </div>
          <Menu :events="menuEvents" :disabled="menuDisabled"></Menu>
        </div>
        <div v-show="Boolean(prompt)" class="chat-bubble" id="discription">{{ prompt }}</div>
      </template>
    </Viewport>
    <PromptInput prompt-type="Story" placeholder="请输入故事描述"></PromptInput>
  </div>
</template>

<script setup lang="ts" name="StoryPanel">
  import Viewport from '@/components/Viewport.vue';
  import PromptInput from '@/components/PromptInput.vue';
  import Menu from '@/components/Menu.vue';
  import { ref, provide } from "vue";
  import type { MenuEvents } from '@/utils/Types';
  import useStoryStore from '@/store/story';
  import emitter from '@/utils/Emitter';

  const storyStore = useStoryStore();
  const storyDom = ref();
  provide('loadingDom', storyDom);

  // menu
  const menuDisabled = ref(true);
  const preHandler = () => menuDisabled.value = true;
  const postHandler = () => menuDisabled.value = false;
  const menuEvents: MenuEvents = {
    editEvent() {
      console.log(11111);
    },
    settingEvent() {
      console.log(33333);
    },
    deleteEvent() {
      console.log(22222);
    },
    extractEvent() {
      emitter.emit('sharePicturePromptPrompt', storyStore.content);
    }
  };
</script>

<style scoped>
  #storyPanel {
    height: 50%;
    justify-content: center;
    display: flex;
    border-bottom: 1px solid #91acb7;
    flex-direction: column;
  }

  .chat-bubble {
    background-color: #91acb7;
    padding: 5px;
    margin-bottom: 10px;
    border-radius: 5px;
    max-width: 94%;
    word-wrap: break-word;
    color: #fff;
  }

  #story {
    text-indent: 2em;
    height: 86%;
    padding: 0 5px 5px 5px;
  }

  .StoryParagraphs {
    text-indent: 2em;
  }

  #title {
    font-weight: bolder;
    font-size: 18px;
    height: 9%;
  }

  #content {
    overflow-x: hidden;
    overflow-y: auto;
    height: 91%;
  }

  #discription {
    background-color: #56a859;
    align-self: flex-end;
    position: sticky;
    top: calc(100% - 23px);
    left: 100%;
    margin-bottom: 3px;
  }
</style>