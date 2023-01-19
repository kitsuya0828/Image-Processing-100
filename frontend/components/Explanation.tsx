import React, { useEffect, useState } from "react";
import { useUserStore } from "./stores/userStore";
import shallow from "zustand/shallow";
import { Button, Group, Modal, ScrollArea, Text } from "@mantine/core";
import { Prism } from "@mantine/prism";
import { getCode } from "./utils/getData";
import { IconLink } from "@tabler/icons";

export const Explanation = () => {
  const [opened, setOpened] = useState(false);
  const [sampleCode, setSampleCode] = useState("");
  const [url, setUrl] = useState("");
  const { questionNumber } = useUserStore(
    (state) => ({
      questionNumber: state.questionNumber,
    }),
    shallow
  );

  useEffect(() => {
    (async () => {
      const endpoint = `code/q${questionNumber}`;
      const response = await getCode(endpoint);
      if (response.status == 1) {
        setSampleCode(response.code);
      } else {
        setSampleCode("");
      }
      setUrl(
        `https://github.com/Kitsuya0828/Image-Processing-100/blob/main/backend/routers/
          q${Math.floor(questionNumber / 10) * 10 + 1}_${
          Math.floor(questionNumber / 10) * 10 + 10
        }/q${questionNumber}.py`
      );
    })();
  }, [opened, questionNumber]);

  return (
    <>
      <Modal
        opened={opened}
        onClose={() => setOpened(false)}
        title={
          <Button variant="subtle" component="a" href={url}>
            <Group spacing="xs">
              <IconLink />
              <Text>サンプルコード</Text>
            </Group>
          </Button>
        }
        centered
        size="xl"
      >
        <ScrollArea style={{ height: "80vh" }} type="always" offsetScrollbars>
          <Prism colorScheme="dark" language="python" withLineNumbers>
            {sampleCode}
          </Prism>
        </ScrollArea>
      </Modal>
      <Group position="right">
        <Button onClick={() => setOpened(true)}>サンプルコード</Button>
      </Group>
    </>
  );
};
