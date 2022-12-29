import create from "zustand";
import { devtools } from "zustand/middleware";

interface UserState {
    questionNumber: number;
    setQuestionNumber: (x: number) => void;
}

export const useUserStore = create<UserState>((set) => ({
  questionNumber: 0,
  setQuestionNumber: (x: number) =>
    set((state) => ({
      ...state,
      questionNumber: x,
    })),
}));