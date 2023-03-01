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
    "Smoothing Filter",
    "Motion Filter",
    "MAX_MIN Filter",
    "Differential Filter",
    "Sobel Filter",
    "Prewitt Filter",
    "Laplacian Filter",
    "Emboss Filter",
    "LoG Filter",
    "Histogram Display",
    "Histogram Normalization",
    "Histogram Operation",
    "Histogram Equalization",
    "Gamma Correction",
    "Nearest Neighbor Interpolation",
    "Bi-linear Interpolation",
    "Bi-cubic Interpolation",
    "Affine transformation (Translation)",
    "Affine transformation (Scaling)",
    "Affine transformation (Rotation)"
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
    "平滑化フィルタ",
    "モーションフィルタ",
    "MAX-MINフィルタ",
    "微分フィルタ",
    "Sobelフィルタ",
    "Prewittフィルタ",
    "Laplacianフィルタ",
    "Embossフィルタ",
    "LoGフィルタ",
    "ヒストグラム表示",
    "ヒストグラム正規化",
    "ヒストグラム操作",
    "ヒストグラム平坦化",
    "ガンマ補正",
    "最近傍補間",
    "Bi-linear補間",
    "Bi-cubic補間",
    "アフィン変換（平行移動）",
    "アフィン変換（拡大縮小）",
    "アフィン変換（回転）",
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
    "Question_11_20#q11-平滑化フィルタ",
    "Question_11_20#q12-モーションフィルタ",
    "Question_11_20#q13-max-minフィルタ",
    "Question_11_20#q14-微分フィルタ",
    "Question_11_20#q15-sobelフィルタ",
    "Question_11_20#q16-prewittフィルタ",
    "Question_11_20#q17-laplacianフィルタ",
    "Question_11_20#q18-embossフィルタ",
    "Question_11_20#q19-logフィルタ",
    "Question_11_20#q20-ヒストグラム表示",
    "Question_21_30#q21-ヒストグラム正規化",
    "Question_21_30#q22-ヒストグラム操作",
    "Question_21_30#q23-ヒストグラム平坦化",
    "Question_21_30#q24-ガンマ補正",
    "Question_21_30#q25-最近傍補間",
    "Question_21_30#q26-bi-linear補間",
    "Question_21_30#q27-bi-cubic補間",
    "Question_21_30#q28-アフィン変換平行移動",
    "Question_21_30#q29-アフィン変換拡大縮小",
    "uestion_21_30#q30-アフィン変換回転",
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
