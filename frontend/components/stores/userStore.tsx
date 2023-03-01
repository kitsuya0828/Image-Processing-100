import create from "zustand";

interface UserState {
    questionNumber: number;
    navbarOpened: boolean;
    setQuestionNumber: (x: number) => void;
    setNavbarOpened: (opened: boolean) => void;
}

export const useUserStore = create<UserState>((set) => ({
  questionNumber: 1,
  navbarOpened: false,
  setQuestionNumber: (x: number) =>
    set((state) => ({
      ...state,
      questionNumber: x,
    })),
  setNavbarOpened: (opened: boolean) =>
    set((state) => ({
      ...state,
      navbarOpened: opened
    })),
}));