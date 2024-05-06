<template>
    <div class="Panel" id="MiddlePanel">
        <Viewport type="Pictures" info="图片" :data-store="pictureStore">
            <template #default="{ showResult }">
                <div v-show="showResult" id="pictures" ref="pictureDom">
                    <div v-for="(pictures, index) in pictureStore.pictures">
                        <p>aaaaaa</p>
                        <div>
                            <img v-for="picture in pictures" :src="picture" />
                        </div>
                    </div>
                </div>
            </template>
        </Viewport>
        <PromptInput input-type="textarea" prompt-type="Pictures" :autosize="true" placeholder="请输入图片描述" />
    </div>
</template>

<script setup lang="ts" name="MiddlePanel">
    import Viewport from '@/components/Viewport.vue';
    import PromptInput from '@/components/PromptInput.vue';
    import usePictureStore from '@/store/pictures';
    import usePicturePromptStore from '@/store/picture-prompt';
    import { ref, provide } from 'vue';

    const pictureStore = usePictureStore();
    const picturePromptStore = usePicturePromptStore();
    const pictureDom = ref();
    provide('loadingDom', pictureDom);
</script>

<style scoped>
    #MiddlePanel {
        width: 50%;
        border-left: 1px solid #91acb7;
        border-right: 1px solid #91acb7;
    }

    #pictures {
        width: 100%;
        height: 100%;
        overflow-y: auto;
    }
</style>
