import { ActionIcon, Button, Loader, Stack, TextInput } from "@mantine/core";
import axios from "axios";
import React, { useState } from "react";
import { IconSquareRoundedX } from "@tabler/icons";
import { ImageDropzone } from "./ImageDropzone";

import { NavbarNested } from "./pages/Navbar";
import { AppShell } from "@mantine/core";
import { Explanation } from "./Explanation";
import { Info } from "./Info";
import { useMediaQuery } from "@mantine/hooks";

export const App = () => {
  const sm = useMediaQuery('(min-width: 768px)')

  return (
    <AppShell
      padding="md"
      navbar={sm ? <NavbarNested /> : <></>}
      // header={<Header height={60} p="xs">{/* Header content */}</Header>}
      styles={(theme) => ({
        main: {
          backgroundColor:
            theme.colorScheme === "dark" ? theme.colors.dark[8] : theme.colors.gray[0],
        },
      })}
    >
      <Stack>
        <Info />
        <ImageDropzone />
        <Explanation />
      </Stack>
    </AppShell>
  );
};
