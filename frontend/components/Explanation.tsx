import React from "react";
import { useUserStore } from "./stores/userStore";
import shallow from "zustand/shallow";

export const Explanation = () => {
  const { questionNumber } = useUserStore(
    (state) => ({
      questionNumber: state.questionNumber,
    }),
    shallow
  );

  return <div>Explanation{questionNumber}</div>;
};
