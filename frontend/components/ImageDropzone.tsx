import { Text, useMantineTheme, Image, SimpleGrid, Stack, LoadingOverlay } from "@mantine/core";
import { Dropzone, DropzoneProps, IMAGE_MIME_TYPE, FileWithPath } from "@mantine/dropzone";
import { useEffect, useState } from "react";
import { postData } from "./utils/getData";
import { useUserStore } from "./stores/userStore";
import shallow from "zustand/shallow";

const url = "http://127.0.0.1:8000/files/";
const switchableQuestionNumbers = [14];

export const ImageDropzone = (props: Partial<DropzoneProps>) => {
  const theme = useMantineTheme();

  const { questionNumber } = useUserStore(
    (state) => ({
      questionNumber: state.questionNumber,
    }),
    shallow
  );

  const isSwitchable = switchableQuestionNumbers.includes(questionNumber);

  const [beforeUrl, setBeforeUrl] = useState("");
  const [afterUrl, setAfterUrl] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if ([9, 10].includes(questionNumber)) {
      setBeforeUrl(`${url}sample/imori_noise.jpeg`);
    } else {
      setBeforeUrl(`${url}sample/imori.jpeg`);
    }
    setAfterUrl(`${url}sample/q${questionNumber}${isSwitchable ? "_v" : ""}.jpg`);
  }, [isSwitchable, questionNumber]);

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
        <SimpleGrid cols={isSwitchable ? 3 : 2}>
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
          ) : (
            <Image radius="md" src={afterUrl} caption={<>After</>} alt="After" />
          )}
        </SimpleGrid>
      </Stack>
    </Dropzone>
  );
};
