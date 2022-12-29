import React from "react";
import { useUserStore } from "./stores/userStore";
import shallow from "zustand/shallow";
import { Flex, Title, Text, createStyles, Group, ActionIcon } from "@mantine/core";
import { IconLink } from "@tabler/icons";

const useStyles = createStyles((theme) => ({
  title: {
    borderBottom: `1px solid ${
      theme.colorScheme === "dark" ? theme.colors.dark[4] : theme.colors.gray[3]
    }`,
  },
}));

export const titleEn = [
    "Channel swapping",
    "Grayscale",
    "Binarization",
    "Binarization of Otsu",
    "HSV Conversion",
    "Discretization of Color",
    "Average Pooling",
    "Max Pooling",
    "Gaussian Filter",
    "Median Filter",
];

export const titleJa = [
    "チャネル入れ替え",
    "グレースケール化",
    "二値化",
    "大津の二値化",
    "HSV変換",
    "減色処理",
    "平均プーリング",
    "Maxプーリング",
    "ガウシアンフィルタ",
    "メディアンフィルタ",
];

const urlJa = [
    "Question_01_10#q1-チャネル入れ替え",
    "Question_01_10#q2-グレースケール化",
    "Question_01_10#q3-二値化",
    "Question_01_10#q4-大津の二値化",
    "Question_01_10#q5-hsv変換",
    "Question_01_10#q6-減色処理",
    "Question_01_10#q7-平均プーリング",
    "Question_01_10#q8-maxプーリング",
    "Question_01_10#q9-ガウシアンフィルタ",
    "Question_01_10#q10-メディアンフィルタ",
];

export const Info = () => {
  const { classes } = useStyles();
  const { questionNumber } = useUserStore(
    (state) => ({
      questionNumber: state.questionNumber,
    }),
    shallow
  );

  return (
    <Flex justify="space-between" align="flex-end" className={classes.title}>
      <Group spacing="xs">
        <ActionIcon
          size="xs"
          component="a"
          href={`https://github.com/ryoppippi/Gasyori100knock/tree/master/${
            urlJa[questionNumber - 1]
          }`}
        >
          <IconLink />
        </ActionIcon>
        <Title color="gray">
          Q{questionNumber}. {titleEn[questionNumber - 1]}
        </Title>
      </Group>
      <Text size="xs" color="gray">
        {titleJa[questionNumber - 1]}
      </Text>
    </Flex>
  );
};
