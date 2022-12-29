import { Group, Text, useMantineTheme, Image, SimpleGrid, Button } from "@mantine/core";
import { IconUpload, IconPhoto, IconX } from "@tabler/icons";
import { Dropzone, DropzoneProps, IMAGE_MIME_TYPE, FileWithPath } from "@mantine/dropzone";
import { useState } from "react";
import axios from "axios";
import { postData } from "./utils/getData";

export const ImageDropzone = (props: Partial<DropzoneProps>) => {
  const [files, setFiles] = useState<FileWithPath[]>([]);
  const theme = useMantineTheme();
  const [url, setUrl] = useState("");

  const previews = files.map((file, index) => {
    const imageUrl = URL.createObjectURL(file);
    return (
      <Image
        key={index}
        src={url ? url : imageUrl}
        imageProps={{ onLoad: () => URL.revokeObjectURL(imageUrl) }}
      />
    );
  });

  const onSubmitImage = async () => {
    if (files.length) {
      const data = new FormData();
      data.append("fileb", files[0]);
      const endpoint = "solve/q1";
      const response = await postData(endpoint, data);
      setUrl("/db/" + response.path);
    }
  };

  return (
    <>
      <Dropzone
        onDrop={setFiles}
        onReject={(files) => console.log("rejected files", files)}
        // maxSize={3 * 1024 ** 2}
        accept={IMAGE_MIME_TYPE}
        multiple={false}
        {...props}
      >
        <Group position="center" spacing="xl" style={{ minHeight: 220, pointerEvents: "none" }}>
          <Dropzone.Accept>
            <IconUpload
              size={50}
              stroke={1.5}
              color={theme.colors[theme.primaryColor][theme.colorScheme === "dark" ? 4 : 6]}
            />
          </Dropzone.Accept>
          <Dropzone.Reject>
            <IconX
              size={50}
              stroke={1.5}
              color={theme.colors.red[theme.colorScheme === "dark" ? 4 : 6]}
            />
          </Dropzone.Reject>
          <Dropzone.Idle>
            <IconPhoto size={50} stroke={1.5} />
          </Dropzone.Idle>

          <div>
            <Text size="md" inline>
              Drag an image here or click to select a file
            </Text>
          </div>
        </Group>
      </Dropzone>

      <SimpleGrid
        cols={4}
        breakpoints={[{ maxWidth: "sm", cols: 1 }]}
        mt={previews.length > 0 ? "xl" : 0}
      >
        {previews}
      </SimpleGrid>
      <Button onClick={onSubmitImage}>送信</Button>
    </>
  );
};
