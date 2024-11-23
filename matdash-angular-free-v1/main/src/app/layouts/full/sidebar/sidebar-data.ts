import { NavItem } from './nav-item/nav-item';

export const navItems: NavItem[] = [
  {
    navCap: 'Home',
  },
  {
    displayName: 'Dashboard',
    iconName: 'solar:widget-add-line-duotone',
    route: '/dashboard',
  },
   {
    navCap: 'Additional Functions',
    divider: true
  },
  {
    displayName: 'Add to Fleet',
    iconName: 'solar:archive-minimalistic-line-duotone',
    route: '/ui-components/badge',
  },
  {
    displayName: 'User Reviews',
    iconName: 'solar:danger-circle-line-duotone',
    route: '/ui-components/chips',
  },
  {
    displayName: 'Bookmarks',
    iconName: 'solar:bookmark-square-minimalistic-line-duotone',
    route: '/ui-components/lists',
  },
  {
    displayName: 'System Changes',
    iconName: 'solar:file-text-line-duotone',
    route: '/ui-components/menu',
  },
 /*  {
    displayName: '',
    iconName: 'solar:text-field-focus-line-duotone',
    route: '/ui-components/tooltips',
  }, */
  {
    displayName: 'Ticket Creation',
    iconName: 'solar:file-text-line-duotone',
    route: '/ui-components/forms',
  },
  {
    displayName: 'Admin Console',
    iconName: 'solar:tablet-line-duotone',
    route: '/ui-components/tables',
  },
  {
    navCap: 'Auth',
    divider: true
  },
  {
    displayName: 'Login',
    iconName: 'solar:login-3-line-duotone',
    route: '/authentication/login',
  },
  {
    displayName: 'Register',
    iconName: 'solar:user-plus-rounded-line-duotone',
    route: '/authentication/register',
    divider: true
  },
 /*  {
    navCap: 'Extra',
    divider: true
  
  },
  {
    displayName: 'Icons',
    iconName: 'solar:sticker-smile-circle-2-line-duotone',
    route: '/extra/icons',
  },  */
  /* {
    displayName: 'Sample Page',
    iconName: 'solar:planet-3-line-duotone',
    route: '/extra/sample-page',
    divider: true
  }, */
]; 
