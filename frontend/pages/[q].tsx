import { App } from "../components/App";
import { useRouter } from "next/router";
import { useUserStore } from "../components/stores/userStore";
import shallow from "zustand/shallow";
import { useEffect } from "react";
import { useMediaQuery } from "@mantine/hooks";


export default function Home() {
  const sm = useMediaQuery("(min-width: 768px)");
  const router = useRouter();
  const queryNumber = parseInt(router.query.q as string, 10);

  const { setQuestionNumber, setNavbarOpened } = useUserStore(
    (state) => ({
      setQuestionNumber: state.setQuestionNumber,
      setNavbarOpened: state.setNavbarOpened,
    }),
    shallow
  );

  useEffect(() => {
    setQuestionNumber(queryNumber);
    if (!sm) {
      setNavbarOpened(false)
    };
  }, [queryNumber, setQuestionNumber])

  return (
    <>
      <App />
    </>
  );
}
