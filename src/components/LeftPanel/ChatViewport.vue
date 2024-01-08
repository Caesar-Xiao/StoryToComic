<template>
    <div id="chatViewport">
        <div v-show="showStory" class="chat-bubble" id="story" ref="storyDom">
            <div id="title"> {{ storyStore.title }} </div>
            <div id="content"> {{ storyStore.content }} </div>
            <Menu :events="menuEvents" :disabled="menuDisabled"></Menu>
        </div>
        <div v-show="Boolean(discription)" class="chat-bubble" id="discription">{{ discription }}</div>
    </div>
</template>

<script setup lang="ts" name="ChatViewport">
    import { ref, watch } from "vue";
    import emitter from '@/utils/Emitter';
    import callPthon from "@/utils/PythonCaller";
    import { ElMessage, ElLoading } from 'element-plus';
    import loadTextFile from "@/utils/LoadTextFile";
    import type { StoryTextObject, MenuEvents } from '@/utils/Types';
    import useStoryStore from '@/store/story';
    import Menu from '../Menu.vue';

    // story
    const storyDom = ref();
    const storyStore = useStoryStore();
    const showStory = ref(false);
    const loadStory = () => {
        loadTextFile('load-story', (story: StoryTextObject) => {
            Object.assign(storyStore, story);
            if (storyStore.error)
                ElMessage(`故事读取失败！\n${storyStore.error}`);
        });
    };
    function setLoading() {
        return ElLoading.service({
            target: storyDom.value,
            lock: true,
            text: '故事生成中...',
            background: '#ebeef5',
        });
    }

    // menu
    const menuDisabled = ref(true);
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
    };


    // discription
    const discription = ref('');

    emitter.on('shareStoryPrompt', (prompt: string) => discription.value = prompt);
    watch(discription, (value: string) => {
        const loading = setLoading();
        showStory.value = true;
        menuDisabled.value = true;
        emitter.emit('setSendButtonStatus', true);

        callPthon('GenerateStory', value,
            (res: string) => {
                if (res === 'Over')
                    loadStory();
                else {
                    showStory.value = false;
                    ElMessage(`故事生成失败！\n${res}`);
                }

                loading.close();
                menuDisabled.value = false;
                emitter.emit('setSendButtonStatus', false);
            });
    });
</script>

<style scoped>
    #chatViewport {
        width: 100%;
        padding: 10px;
        height: calc(100% - 42px);
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
        height: 86%;
        padding: 0 5px 5px 5px;
    }

    #title {
        font-weight: bold;
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