<template>
    <div class="ChildPanel" id="picturePromptViewport">
        <Viewport type="Picture-Prompt" info="提示词" :data-store="picturePromptStore">
            <template #default="{ showResult }">
                <div v-show="showResult" id="picturePrompt" ref="picturePromptDom">
                    <div v-for="prompt in picturePromptStore.prompts" class="promptDisplay">
                        <p class="originalText">{{ prompt.content }}</p>
                        <p class="promptText">{{ prompt.prompt }}</p>
                    </div>
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
    import usePicturePromptStore from '@/store/picture-rompt';

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
        height: 100%;
        overflow-y: auto;
    }

    .promptDisplay {
        text-indent: 2em;
        margin-bottom: 15px;
        color: white;
    }

    .originalText{
        border-radius: 5px;
        padding: 0 5px 5px 5px;
        background-color: #91acb7;
        margin-bottom: 5px;
    }

    .promptText{
        border-radius: 5px;
        padding: 0 5px 5px 5px;
        background-color: #56a859;
    }
</style>