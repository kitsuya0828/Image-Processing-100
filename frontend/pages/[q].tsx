import { App } from "../components/App";
import { useRouter } from "next/router";
import { useUserStore } from "../components/stores/userStore";
import shallow from "zustand/shallow";
import { useEffect } from "react";


export default function Home() {

  const router = useRouter();
  const queryNumber = parseInt(router.query.q as string, 10);

  const { setQuestionNumber } = useUserStore(
    (state) => ({
      setQuestionNumber: state.setQuestionNumber,
    }),
    shallow
  );

  useEffect(() => {
    setQuestionNumber(queryNumber);
  }, [queryNumber, setQuestionNumber])

  return (
    <>
      <App />
    </>
  );
}
