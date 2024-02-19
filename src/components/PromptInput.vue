<template>
    <div id="promptInput">
        <el-input v-model="prompt" :placeholder=placeholder :type="inputType" :autosize="autosize" :resize="resize" />
        <img v-if="!sendDisabled" @click="sendPrompt" src="@/assets/images/send.png">
        <img v-if="sendDisabled" id="disabled" src="@/assets/images/send-disabled.png">
    </div>
</template>

<script setup lang="ts" name="PromptInput">
    import { ref } from 'vue';
    import emitter from '@/utils/Emitter';

    // input
    const prompt = ref('');
    const props = defineProps({
        inputType: {
            required: false,
            type: String,
            default: 'text'
        },
        promptType: {
            required: false,
            type: String,
            default: ''
        },
        autosize: {
            required: false,
            type: Boolean,
            default: false
        },
        resize: {
            required: false,
            type: String,
            default: 'none'
        },
        placeholder: {
            required: false,
            type: String,
            default: '请输入'
        }
    });

    function sendPrompt() {
        emitter.emit(`share${props.promptType}Prompt`, prompt.value);
        prompt.value = '';
    }


    // button
    const sendDisabled = ref(false);
    emitter.on('setSendButtonStatus', (status: boolean) => sendDisabled.value = status);
</script>

<style scoped>
    #promptInput {
        display: flex;
        justify-content: center;
        align-items: center;
        width: calc(100% - 10px);
        margin: 5px;
    }

    img {
        width: 30px;
        margin-left: 5px;
        cursor: pointer;
    }

    #disabled {
        cursor: not-allowed;
    }

    .el-input {
        --el-input-focus-border: #rgb(178, 197, 205);
        --el-input-focus-border-color: #91acb7;
    }
</style>