import { ActionIcon, Button, Loader, TextInput } from "@mantine/core";
import axios from "axios";
import React, { useState } from "react";
import { IconSquareRoundedX } from "@tabler/icons";
import { ImageDropzone } from "./ImageDropzone";

import { NavbarNested } from "./pages/Navbar";
import { AppShell } from "@mantine/core";

export const App = () => {
  return (
    <AppShell
      padding="md"
      navbar={<NavbarNested />}
      // header={<Header height={60} p="xs">{/* Header content */}</Header>}
      styles={(theme) => ({
        main: {
          backgroundColor:
            theme.colorScheme === "dark" ? theme.colors.dark[8] : theme.colors.gray[0],
        },
      })}
    >
      <ImageDropzone />
    </AppShell>
  );
};
