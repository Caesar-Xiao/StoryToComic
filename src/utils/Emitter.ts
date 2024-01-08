import mitt, { type Emitter } from "mitt";
import { type EmitterEvents } from './Types';

const emitter: Emitter<EmitterEvents> = mitt<EmitterEvents>();

export default emitter;