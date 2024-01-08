import { defineStore } from "pinia";

const useStoryStore = defineStore('story', {
    state() {
        return {
            title: '',
            content: '',
            error: null,
        };
    },
    // getters:{
    //     getStories(state){
    //         return state.stories;
    //     }
    // },
    // actions:{
    //     setStories(state, stories){
    //         state.stories = stories;
    //     }
    // }
});

export default useStoryStore;