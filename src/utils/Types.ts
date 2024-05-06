export type EmitterEvents = {
    [propName: string]: any;
};

export interface StoryTextObject {
    title: string;
    content: string;
    error: any;
}

export interface MenuEvents {
    editEvent?: Function;
    deleteEvent?: Function;
    settingEvent?: Function;
    extractEvent?: Function;
}

export interface PicturePromptObject {
    prompts: PicturePromptType;
    error: any;
}

export interface PicturePromptType {
    content: string;
    prompt: string;
}

export interface PicturesObject {
    pictures: string[][];
    error: any;
}

export interface PicturePromptStore {
    error: any;
    prompts: PicturePromptType[];
}

