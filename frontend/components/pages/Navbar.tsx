import {
  Code,
  createStyles,
  Group,
  Navbar,
  ScrollArea,
  Title,
  UnstyledButton,
  Text,
  ActionIcon,
  Flex,
} from "@mantine/core";
import {
  IconNotes,
  IconCalendarStats,
  IconGauge,
  IconChevronLeft,
  IconPresentationAnalytics,
  IconFileAnalytics,
  IconAdjustments,
  IconLock,
  IconBrandGithub,
  IconChevronRight,
} from "@tabler/icons";
import { LinksGroup } from "./NavbarLinksGroup";
import { titleJa } from "../Info";
import { useUserStore } from "../stores/userStore";
import shallow from "zustand/shallow";
import Link from "next/link";
import { useMediaQuery } from "@mantine/hooks";

const mockdata = [
  {
    label: "問題1-10",
    icon: IconGauge,
    links: [...Array(10)].map((_, num) => ({ label: titleJa[num], link: (num + 1).toString() })),
  },
  {
    label: "問題11-20",
    icon: IconGauge,
    links: [...Array(10)].map((_, num) => ({
      label: titleJa[num + 10],
      link: (num + 11).toString(),
    })),
  },
  {
    label: "問題21-30",
    icon: IconGauge,
    links: [...Array(10)].map((_, num) => ({
      label: titleJa[num + 20],
      link: (num + 21).toString(),
    })),
  },
  {
    label: "問題31-40",
    icon: IconCalendarStats,
    links: [
      { label: "Upcoming releases", link: "/" },
      { label: "Previous releases", link: "/" },
      { label: "Releases schedule", link: "/" },
    ],
  },
  { label: "問題41-50", icon: IconFileAnalytics },
  { label: "問題51-60", icon: IconAdjustments },
  {
    label: "問題61-70",
    icon: IconLock,
    links: [
      { label: "Enable 2FA", link: "/" },
      { label: "Change password", link: "/" },
      { label: "Recovery codes", link: "/" },
    ],
  },
  {
    label: "問題71-80",
    icon: IconLock,
    links: [
      { label: "Enable 2FA", link: "/" },
      { label: "Change password", link: "/" },
      { label: "Recovery codes", link: "/" },
    ],
  },
  { label: "問題81-90", icon: IconFileAnalytics },
  { label: "問題91-100", icon: IconAdjustments },
];

const useStyles = createStyles((theme) => ({
  navbar: {
    backgroundColor: theme.colorScheme === "dark" ? theme.colors.dark[6] : theme.white,
    paddingBottom: 0,
  },

  header: {
    padding: theme.spacing.md,
    marginLeft: -theme.spacing.md,
    marginRight: -theme.spacing.md,
    marginTop: -theme.spacing.md,
    color: theme.colorScheme === "dark" ? theme.white : theme.black,
    borderBottom: `1px solid ${
      theme.colorScheme === "dark" ? theme.colors.dark[4] : theme.colors.gray[3]
    }`,
  },

  links: {
    marginLeft: -theme.spacing.md,
    marginRight: -theme.spacing.md,
  },

  linksInner: {
    paddingTop: theme.spacing.xl,
    paddingBottom: theme.spacing.xl,
  },

  footer: {
    marginLeft: -theme.spacing.md,
    marginRight: -theme.spacing.md,
    marginBottom: -theme.spacing.md,
    borderTop: `1px solid ${
      theme.colorScheme === "dark" ? theme.colors.dark[4] : theme.colors.gray[3]
    }`,
  },

  author: {
    fontWeight: 500,
    display: "block",
    width: "100%",
    padding: `${theme.spacing.xs}px ${theme.spacing.md}px`,
    color: theme.colorScheme === "dark" ? theme.colors.dark[0] : theme.black,
    fontSize: theme.fontSizes.sm,

    "&:hover": {
      backgroundColor: theme.colorScheme === "dark" ? theme.colors.dark[7] : theme.colors.gray[0],
      color: theme.colorScheme === "dark" ? theme.white : theme.black,
    },
  },
}));

export const NavbarNested = () => {
  const { classes } = useStyles();
  const sm = useMediaQuery("(min-width: 768px)")
  const links = mockdata.map((item) => <LinksGroup {...item} key={item.label} />);

  const { navbarOpened, setNavbarOpened } = useUserStore(
    (state) => ({
      navbarOpened: state.navbarOpened,
      setNavbarOpened: state.setNavbarOpened,
    }),
    shallow
  );

  return navbarOpened ? (
    <Navbar style={{ width: sm ? "250px" : "80vw" }} p="md" className={classes.navbar}>
      <Navbar.Section className={classes.header}>
        <Flex justify="flex-end" direction="row" wrap="wrap">
          <ActionIcon onClick={() => setNavbarOpened(false)}>
            <IconChevronLeft />
          </ActionIcon>
        </Flex>
        <Group position="apart">
          <Link
            href={{
              pathname: "/",
            }}
            style={{ textDecoration: "none" }}
          >
            <Title size={30} variant="gradient" gradient={{ from: "indigo", to: "cyan", deg: 45 }}>
              Image Processing 100 Questions
            </Title>
          </Link>
        </Group>
      </Navbar.Section>

      <Navbar.Section grow className={classes.links} component={ScrollArea}>
        <div className={classes.linksInner}>{links}</div>
      </Navbar.Section>

      <Navbar.Section className={classes.footer}>
        <UnstyledButton
          component="a"
          href="https://github.com/Kitsuya0828"
          className={classes.author}
        >
          <Group>
            <IconBrandGithub />
            <div>
              <Text>Kitsuya Azuma</Text>
              <Code sx={{ fontWeight: 700, color: "gray" }}>@Kitsuya0828</Code>
            </div>
          </Group>
        </UnstyledButton>
      </Navbar.Section>
    </Navbar>
  ) : (
    <ActionIcon onClick={() => setNavbarOpened(true)}>
      <IconChevronRight />
    </ActionIcon>
  );
};
