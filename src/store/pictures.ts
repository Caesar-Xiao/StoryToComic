import { defineStore } from "pinia";

const usePictureStore = defineStore("pictures", {
    state() {
        const pictures: string[][] = [];

        return {
            error: null,
            pictures
        };
    }
});

export default usePictureStore;