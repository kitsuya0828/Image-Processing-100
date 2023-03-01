import { NavbarNested } from "../components/pages/Navbar";

import {
  createStyles,
  Image,
  Container,
  Title,
  Button,
  Group,
  Text,
  List,
  ThemeIcon,
  AppShell,
} from "@mantine/core";
import { IconCheck } from "@tabler/icons";
import Link from "next/link";

const useStyles = createStyles((theme) => ({
  inner: {
    display: "flex",
    justifyContent: "space-between",
    paddingTop: theme.spacing.xl * 4,
    paddingBottom: theme.spacing.xl * 4,
  },

  content: {
    maxWidth: 480,
    marginRight: theme.spacing.xl * 3,

    [theme.fn.smallerThan("md")]: {
      maxWidth: "100%",
      marginRight: 0,
    },
  },

  title: {
    color: theme.colorScheme === "dark" ? theme.white : theme.black,
    fontFamily: `Greycliff CF, ${theme.fontFamily}`,
    fontSize: 44,
    lineHeight: 1.2,
    fontWeight: 900,

    [theme.fn.smallerThan("xs")]: {
      fontSize: 28,
    },
  },

  control: {
    [theme.fn.smallerThan("xs")]: {
      flex: 1,
    },
  },

  image: {
    flex: 1,

    [theme.fn.smallerThan("md")]: {
      display: "none",
    },
  },

  highlight: {
    position: "relative",
    backgroundColor: theme.fn.variant({ variant: "light", color: theme.primaryColor }).background,
    borderRadius: theme.radius.sm,
    padding: "4px 12px",
  },
}));

export default function Home() {
  const { classes } = useStyles();

  return (
    <AppShell
      padding="md"
      navbar={<NavbarNested />}
      styles={(theme) => ({
        main: {
          backgroundColor:
            theme.colorScheme === "dark" ? theme.colors.dark[8] : theme.colors.gray[0],
        },
      })}
    >
      <Container>
        <div className={classes.inner}>
          <div className={classes.content}>
            <Title className={classes.title}>画像処理100本ノック</Title>
            <Text color="dimmed" mt="md">
              <a href="https://github.com/ryoppippi/Gasyori100knock">画像処理100本ノック</a>のプログラムをブラウザ上で簡単に試せるWebアプリです。
              <br/ >対応するソースコードもブラウザ上から確認できます。
            </Text>

            {/* <List
              mt={30}
              spacing="sm"
              size="sm"
              icon={
                <ThemeIcon size={20} radius="xl">
                  <IconCheck size={12} stroke={1.5} />
                </ThemeIcon>
              }
            >
              <List.Item>
                <b>TypeScript based</b> – build type safe applications, all components and hooks
                export types
              </List.Item>
              <List.Item>
                <b>Free and open source</b> – all packages have MIT license, you can use Mantine in
                any project
              </List.Item>
              <List.Item>
                <b>No annoying focus ring</b> – focus ring will appear only when user navigates with
                keyboard
              </List.Item>
            </List> */}

            <Group mt={30}>
              <Link
                href={{
                  pathname: "[q]",
                  query: { q: 1 },
                }}
              >
                <Button radius="xl" size="md" className={classes.control}>
                  Get started
                </Button>
              </Link>
              <Button
                component="a"
                variant="default"
                radius="xl"
                size="md"
                className={classes.control}
                href="https://github.com/Kitsuya0828/Image-Processing-100"
                target="_blank"
              >
                Fork me on GitHub
              </Button>
            </Group>
          </div>
          <Image src="/db/sample/imori.png" className={classes.image} />
        </div>
      </Container>
    </AppShell>
  );
}
