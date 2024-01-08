<template>
    <div class="Buttons">
        <el-button :disabled="disabled" @click="events.editEvent" size="small" color="#91acb7" type="primary" circle>
            <el-icon color="white" size="15">
                <Edit />
            </el-icon>
        </el-button>
        <el-button :disabled="disabled" @click="events.settingEvent" size="small" color="#91acb7" type="primary" circle>
            <el-icon color="white" size="15">
                <Setting />
            </el-icon>
        </el-button>
        <el-button :disabled="disabled" @click="events.deleteEvent" size="small" color="#91acb7" type="primary" circle>
            <el-icon color="white" size="15">
                <Delete />
            </el-icon>
        </el-button>
    </div>
</template>

<script setup lang="ts" name="Menu">
    import { Delete, Setting, Edit } from '@element-plus/icons-vue';
    import type { MenuEvents } from '@/utils/Types';

    defineProps<{
        events: MenuEvents;
        disabled: boolean;
    }>();
</script>

<style scoped>
    .Buttons {
        display: flex;
        flex-direction: column;
        position: relative;
        left: 100%;
        bottom: 100%;
        margin-left: 9px;
    }

    .el-button {
        margin: 0 0 5px 0;
    }
</style>