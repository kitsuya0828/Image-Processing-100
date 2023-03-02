import { Text, useMantineTheme, Image, SimpleGrid, Stack, LoadingOverlay } from "@mantine/core";
import { Dropzone, DropzoneProps, IMAGE_MIME_TYPE, FileWithPath } from "@mantine/dropzone";
import { useEffect, useState } from "react";
import { postData } from "./utils/getData";
import { useUserStore } from "./stores/userStore";
import shallow from "zustand/shallow";

const url = `${process.env.NEXT_PUBLIC_BACKEND_URL}/files/`;
const switchableQuestionNumbers = [14, 15, 16];
const multipleQuestionNumbers = [29, 30];
const histgramQuestionNumbers = [21, 22, 23];

export const ImageDropzone = (props: Partial<DropzoneProps>) => {
  const theme = useMantineTheme();

  const { questionNumber } = useUserStore(
    (state) => ({
      questionNumber: state.questionNumber,
    }),
    shallow
  );

  const isSwitchable = switchableQuestionNumbers.includes(questionNumber);
  const isMultiple = multipleQuestionNumbers.includes(questionNumber);
  const isHistgram = histgramQuestionNumbers.includes(questionNumber);

  const [beforeUrl, setBeforeUrl] = useState("");
  const [afterUrl, setAfterUrl] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if ([9, 10, 19].includes(questionNumber)) {
      setBeforeUrl(`${url}sample/imori_noise.jpeg`);
    } else if ([20, 21, 22].includes(questionNumber)) {
      setBeforeUrl(`${url}sample/imori_dark.jpeg`);
    } else if (questionNumber === 24) {
      setBeforeUrl(`${url}sample/imori_gamma.jpeg`);
    } else {
      setBeforeUrl(`${url}sample/imori.jpeg`);
    }
    setAfterUrl(`${url}sample/q${questionNumber}${isSwitchable ? "_v" : isMultiple ? "_1" : ""}.jpg`);
  }, [isSwitchable, questionNumber, isMultiple]);

  const endpoint = `solve/q${questionNumber}`;

  const onSubmitImage = async (droppedFiles: FileWithPath[], endpoint: string) => {
    if (droppedFiles.length) {
      setLoading(true);
      const imageUrl = URL.createObjectURL(droppedFiles[0]);
      setBeforeUrl(imageUrl);

      const data = new FormData();
      data.append("fileb", droppedFiles[0]);
      const response = await postData(endpoint, data);

      if (response.status == 1) {
        setAfterUrl(url + response.path);
      }
      setLoading(false);
    }
  };

  return (
    <Dropzone
      onDrop={(droppedFiles) => {
        onSubmitImage(droppedFiles, endpoint);
      }}
      accept={IMAGE_MIME_TYPE}
      multiple={false}
      {...props}
    >
      <Stack align="center">
        <Text size="xs" color="dimmed" inline>
          Drag an image here or click to select a file
        </Text>
        <SimpleGrid cols={isSwitchable || isHistgram || isMultiple ? 3 : 2}>
          <Image radius="md" src={beforeUrl} caption="Before" alt="Before" />
          {loading ? (
            <LoadingOverlay transitionDuration={500} visible={true} />
          ) : isSwitchable ? (
            <>
              <Image radius="md" src={afterUrl} caption="After (Vertical)" alt="After (Vertical)" />
              <Image
                radius="md"
                src={afterUrl.replace("_v", "_h")}
                caption="After (Horizontal)"
                alt="After (Horizontal)"
              />
            </>
          ) : isMultiple ? (
            <>
              <Image radius="md" src={afterUrl} caption="After (1)" alt="After (1)" />
              <Image
                radius="md"
                src={afterUrl.replace("_1", "_2")}
                caption="After (2)"
                alt="After (2)"
              />
            </>
          ) : isHistgram ? (
            <>
              <Image radius="md" src={afterUrl} caption="After" alt="After" />
              <Image
                radius="md"
                src={afterUrl.replace(".jpg", "_hist.jpg")}
                caption="After (Histogram)"
                alt="After (Histogram)"
              />
            </>
          ) : (
            <Image radius="md" src={afterUrl} caption="After" alt="After" />
          )}
        </SimpleGrid>
      </Stack>
    </Dropzone>
  );
};
