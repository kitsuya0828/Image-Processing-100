import create from "zustand";

interface UserState {
    questionNumber: number;
    setQuestionNumber: (x: number) => void;
}

export const useUserStore = create<UserState>((set) => ({
  questionNumber: 1,
  setQuestionNumber: (x: number) =>
    set((state) => ({
      ...state,
      questionNumber: x,
    })),
}));