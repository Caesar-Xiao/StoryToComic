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
}