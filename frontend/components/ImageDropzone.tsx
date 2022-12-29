import { Text, useMantineTheme, Image, SimpleGrid, Stack } from "@mantine/core";
import { Dropzone, DropzoneProps, IMAGE_MIME_TYPE, FileWithPath } from "@mantine/dropzone";
import { useState } from "react";
import { postData } from "./utils/getData";

export const ImageDropzone = (props: Partial<DropzoneProps>) => {
  const theme = useMantineTheme();
  const [beforeUrl, setBeforeUrl] = useState("/db/sample/imori_256x256.png");
  const [afterUrl, setAfterUrl] = useState("/db/sample/q1.jpg");
  const endpoint = "solve/q1";

  const onSubmitImage = async (droppedFiles: FileWithPath[], endpoint: string) => {
    if (droppedFiles.length) {
      const imageUrl = URL.createObjectURL(droppedFiles[0]);
      setBeforeUrl(imageUrl);

      const data = new FormData();
      data.append("fileb", droppedFiles[0]);
      const response = await postData(endpoint, data);

      if (response.status == 1) {
        setAfterUrl("/db/" + response.path);
      }
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
        <SimpleGrid cols={2}>
          <Image radius="md" src={beforeUrl} caption="Before" />
          <Image radius="md" src={afterUrl} caption="After" />
        </SimpleGrid>
      </Stack>
    </Dropzone>
  );
};
