<template>
    <div id="viewport">
        <slot :prompt="prompt" :showResult="showResult"></slot>
    </div>
</template>

<script setup lang="ts" name="Viewport">
    import { ref, watch, inject, type Ref } from "vue";
    import emitter from '@/utils/Emitter';
    import callPython from "@/utils/PythonCaller";
    import { ElMessage, ElLoading } from 'element-plus';
    import loadTextFile from "@/utils/LoadTextFile";
    import type { StoryTextObject, PicturePromptObject, PicturesObject } from '@/utils/Types';

    const loadingDom = inject('loadingDom') as Ref<any>;
    const { type, info, dataStore, preHandler, postHandler } = defineProps<{
        type: String,
        info: String,
        dataStore: any;
        preHandler?: Function;
        postHandler?: Function;
    }>();

    // result
    const showResult = ref(false);
    const loadResult = () => {
        loadTextFile(`load-${type.toLowerCase()}`, (data: StoryTextObject | PicturePromptObject | PicturesObject) => {
            Object.assign(dataStore, data);
            if (dataStore.error)
                ElMessage(`${info}读取失败！\n${dataStore.error}`);
            console.log(data);
        });
    };
    function setLoading() {
        return ElLoading.service({
            target: loadingDom.value,
            lock: true,
            text: `${info}生成中...`,
            background: '#ebeef5',
        });
    }


    // prompt
    const prompt = ref('');
    const typeStr = type.replace('-', '');
    emitter.on(`share${typeStr}Prompt`, (ppt: string) => prompt.value = ppt);
    watch(prompt, (value: string) => {
        const loading = setLoading();
        showResult.value = true;

        preHandler?.();
        emitter.emit('setSendButtonStatus', true);

        callPython(`Generate${typeStr}`, value,
            (res: string) => {
                if (res === 'Over')
                    loadResult();
                else {
                    showResult.value = false;
                    ElMessage(`${info}生成失败！\n${res}`);
                }

                loading.close();

                postHandler?.();
                emitter.emit('setSendButtonStatus', false);
            });
    });
</script>

<style scoped>
    #viewport {
        width: 100%;
        padding: 10px;
        height: calc(100% - 52px);
    }
</style>