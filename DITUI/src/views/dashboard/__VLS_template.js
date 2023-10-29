import chart from '@images/avatars/avatar-1.png';
import { __VLS_internalComponent, __VLS_componentsOption, __VLS_name, isAdmin, moreList, logs } from './DataLogs.vue';

function __VLS_template() {
let __VLS_ctx!: InstanceType<__VLS_PickNotAny<typeof __VLS_internalComponent, new () => {}>> & {};
/* Components */
let __VLS_otherComponents!: NonNullable<typeof __VLS_internalComponent extends { components: infer C; } ? C : {}> & typeof __VLS_componentsOption;
let __VLS_own!: __VLS_SelfComponent<typeof __VLS_name, typeof __VLS_internalComponent & (new () => { $slots: typeof __VLS_slots; })>;
let __VLS_localComponents!: typeof __VLS_otherComponents & Omit<typeof __VLS_own, keyof typeof __VLS_otherComponents>;
let __VLS_components!: typeof __VLS_localComponents & __VLS_GlobalComponents & typeof __VLS_ctx;
/* Style Scoped */
type __VLS_StyleScopedClasses = {} &
{ 'card-list'?: boolean; };
let __VLS_styleScopedClasses!: __VLS_StyleScopedClasses | keyof __VLS_StyleScopedClasses | (keyof __VLS_StyleScopedClasses)[];
/* CSS variable injection */
/* CSS variable injection end */
let __VLS_resolvedLocalAndGlobalComponents!: {} &
__VLS_WithComponent<'VCard', typeof __VLS_localComponents, "VCard", "VCard", "VCard"> &
__VLS_WithComponent<'MoreBtn', typeof __VLS_localComponents, "MoreBtn", "MoreBtn", "MoreBtn"> &
__VLS_WithComponent<'VCardText', typeof __VLS_localComponents, "VCardText", "VCardText", "VCardText"> &
__VLS_WithComponent<'VList', typeof __VLS_localComponents, "VList", "VList", "VList"> &
__VLS_WithComponent<'VListItem', typeof __VLS_localComponents, "VListItem", "VListItem", "VListItem"> &
__VLS_WithComponent<'VAvatar', typeof __VLS_localComponents, "VAvatar", "VAvatar", "VAvatar"> &
__VLS_WithComponent<'VListItemSubtitle', typeof __VLS_localComponents, "VListItemSubtitle", "VListItemSubtitle", "VListItemSubtitle"> &
__VLS_WithComponent<'VListItemTitle', typeof __VLS_localComponents, "VListItemTitle", "VListItemTitle", "VListItemTitle"> &
__VLS_WithComponent<'VListItemAction', typeof __VLS_localComponents, "VListItemAction", "VListItemAction", "VListItemAction"> &
__VLS_WithComponent<'VChip', typeof __VLS_localComponents, "VChip", "VChip", "VChip">;
__VLS_components.VCard; __VLS_components.VCard;
// @ts-ignore
[VCard, VCard,];
__VLS_intrinsicElements.template; __VLS_intrinsicElements.template; __VLS_intrinsicElements.template; __VLS_intrinsicElements.template; __VLS_intrinsicElements.template; __VLS_intrinsicElements.template;
__VLS_intrinsicElements.div; __VLS_intrinsicElements.div;
__VLS_components.MoreBtn;
// @ts-ignore
[MoreBtn,];
__VLS_components.VCardText; __VLS_components.VCardText;
// @ts-ignore
[VCardText, VCardText,];
__VLS_components.VList; __VLS_components.VList;
// @ts-ignore
[VList, VList,];
__VLS_components.VListItem; __VLS_components.VListItem;
// @ts-ignore
[VListItem, VListItem,];
__VLS_components.VAvatar;
// @ts-ignore
[VAvatar,];
__VLS_components.VListItemSubtitle; __VLS_components.VListItemSubtitle;
// @ts-ignore
[VListItemSubtitle, VListItemSubtitle,];
__VLS_components.VListItemTitle; __VLS_components.VListItemTitle;
// @ts-ignore
[VListItemTitle, VListItemTitle,];
__VLS_components.VListItemAction; __VLS_components.VListItemAction;
// @ts-ignore
[VListItemAction, VListItemAction,];
__VLS_components.VChip; __VLS_components.VChip;
// @ts-ignore
[VChip, VChip,];
{
let __VLS_0!: 'VCard' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VCard : (typeof __VLS_resolvedLocalAndGlobalComponents)['VCard'];
const __VLS_1 = __VLS_asFunctionalComponent(__VLS_0, new __VLS_0({ ...{}, title: (('My Recent Actions' ? __VLS_ctx.isAdmin : 'Recent Actions')), }));
({} as { VCard: typeof __VLS_0; }).VCard;
({} as { VCard: typeof __VLS_0; }).VCard;
const __VLS_2 = __VLS_1({ ...{}, title: (('My Recent Actions' ? __VLS_ctx.isAdmin : 'Recent Actions')), }, ...__VLS_functionalComponentArgsRest(__VLS_1));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_0, typeof __VLS_2> & Record<string, unknown>) => void)({ ...{}, title: (('My Recent Actions' ? __VLS_ctx.isAdmin : 'Recent Actions')), });
const __VLS_3 = __VLS_pickFunctionalComponentCtx(__VLS_0, __VLS_2)!;
let __VLS_4!: __VLS_NormalizeEmits<typeof __VLS_3.emit>;
{
const __VLS_5 = __VLS_intrinsicElements["template"];
const __VLS_6 = __VLS_elementAsFunctionalComponent(__VLS_5);
const __VLS_7 = __VLS_6({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_6));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_5, typeof __VLS_7> & Record<string, unknown>) => void)({ ...{}, });
{
(__VLS_3.slots!).append;
{
const __VLS_8 = __VLS_intrinsicElements["div"];
const __VLS_9 = __VLS_elementAsFunctionalComponent(__VLS_8);
const __VLS_10 = __VLS_9({ ...{}, class: ("me-n3 mt-n2"), }, ...__VLS_functionalComponentArgsRest(__VLS_9));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_8, typeof __VLS_10> & Record<string, unknown>) => void)({ ...{}, class: ("me-n3 mt-n2"), });
const __VLS_11 = __VLS_pickFunctionalComponentCtx(__VLS_8, __VLS_10)!;
let __VLS_12!: __VLS_NormalizeEmits<typeof __VLS_11.emit>;
{
let __VLS_13!: 'MoreBtn' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.MoreBtn : (typeof __VLS_resolvedLocalAndGlobalComponents)['MoreBtn'];
const __VLS_14 = __VLS_asFunctionalComponent(__VLS_13, new __VLS_13({ ...{}, menuList: ((__VLS_ctx.moreList)), }));
({} as { MoreBtn: typeof __VLS_13; }).MoreBtn;
const __VLS_15 = __VLS_14({ ...{}, menuList: ((__VLS_ctx.moreList)), }, ...__VLS_functionalComponentArgsRest(__VLS_14));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_13, typeof __VLS_15> & Record<string, unknown>) => void)({ ...{}, menuList: ((__VLS_ctx.moreList)), });
const __VLS_16 = __VLS_pickFunctionalComponentCtx(__VLS_13, __VLS_15)!;
let __VLS_17!: __VLS_NormalizeEmits<typeof __VLS_16.emit>;
}
(__VLS_11.slots!).default;
}
// @ts-ignore
[isAdmin, isAdmin, isAdmin, moreList, moreList, moreList,];
}
}
{
let __VLS_18!: 'VCardText' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VCardText : (typeof __VLS_resolvedLocalAndGlobalComponents)['VCardText'];
const __VLS_19 = __VLS_asFunctionalComponent(__VLS_18, new __VLS_18({ ...{}, }));
({} as { VCardText: typeof __VLS_18; }).VCardText;
({} as { VCardText: typeof __VLS_18; }).VCardText;
const __VLS_20 = __VLS_19({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_19));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_18, typeof __VLS_20> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_21 = __VLS_pickFunctionalComponentCtx(__VLS_18, __VLS_20)!;
let __VLS_22!: __VLS_NormalizeEmits<typeof __VLS_21.emit>;
{
let __VLS_23!: 'VList' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VList : (typeof __VLS_resolvedLocalAndGlobalComponents)['VList'];
const __VLS_24 = __VLS_asFunctionalComponent(__VLS_23, new __VLS_23({ ...{}, class: ("card-list"), }));
({} as { VList: typeof __VLS_23; }).VList;
({} as { VList: typeof __VLS_23; }).VList;
const __VLS_25 = __VLS_24({ ...{}, class: ("card-list"), }, ...__VLS_functionalComponentArgsRest(__VLS_24));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_23, typeof __VLS_25> & Record<string, unknown>) => void)({ ...{}, class: ("card-list"), });
const __VLS_26 = __VLS_pickFunctionalComponentCtx(__VLS_23, __VLS_25)!;
let __VLS_27!: __VLS_NormalizeEmits<typeof __VLS_26.emit>;
for (const [item] of __VLS_getVForSourceType((__VLS_ctx.logs)!)) {
{
let __VLS_28!: 'VListItem' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VListItem : (typeof __VLS_resolvedLocalAndGlobalComponents)['VListItem'];
const __VLS_29 = __VLS_asFunctionalComponent(__VLS_28, new __VLS_28({ ...{}, key: ((item.timestamp)), }));
({} as { VListItem: typeof __VLS_28; }).VListItem;
({} as { VListItem: typeof __VLS_28; }).VListItem;
const __VLS_30 = __VLS_29({ ...{}, key: ((item.timestamp)), }, ...__VLS_functionalComponentArgsRest(__VLS_29));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_28, typeof __VLS_30> & Record<string, unknown>) => void)({ ...{}, key: ((item.timestamp)), });
const __VLS_31 = __VLS_pickFunctionalComponentCtx(__VLS_28, __VLS_30)!;
let __VLS_32!: __VLS_NormalizeEmits<typeof __VLS_31.emit>;
{
const __VLS_33 = __VLS_intrinsicElements["template"];
const __VLS_34 = __VLS_elementAsFunctionalComponent(__VLS_33);
const __VLS_35 = __VLS_34({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_34));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_33, typeof __VLS_35> & Record<string, unknown>) => void)({ ...{}, });
{
(__VLS_31.slots!).prepend;
{
let __VLS_36!: 'VAvatar' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VAvatar : (typeof __VLS_resolvedLocalAndGlobalComponents)['VAvatar'];
const __VLS_37 = __VLS_asFunctionalComponent(__VLS_36, new __VLS_36({ ...{}, rounded: (true), variant: ("tonal"), color: ((item.color)), image: ((__VLS_ctx.chart)), class: ("me-3"), }));
({} as { VAvatar: typeof __VLS_36; }).VAvatar;
const __VLS_38 = __VLS_37({ ...{}, rounded: (true), variant: ("tonal"), color: ((item.color)), image: ((__VLS_ctx.chart)), class: ("me-3"), }, ...__VLS_functionalComponentArgsRest(__VLS_37));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_36, typeof __VLS_38> & Record<string, unknown>) => void)({ ...{}, rounded: (true), variant: ("tonal"), color: ((item.color)), image: ((__VLS_ctx.chart)), class: ("me-3"), });
const __VLS_39 = __VLS_pickFunctionalComponentCtx(__VLS_36, __VLS_38)!;
let __VLS_40!: __VLS_NormalizeEmits<typeof __VLS_39.emit>;
}
// @ts-ignore
[logs, chart, chart, chart,];
}
}
{
let __VLS_41!: 'VListItemSubtitle' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VListItemSubtitle : (typeof __VLS_resolvedLocalAndGlobalComponents)['VListItemSubtitle'];
const __VLS_42 = __VLS_asFunctionalComponent(__VLS_41, new __VLS_41({ ...{}, class: ("text-disabled mb-1"), }));
({} as { VListItemSubtitle: typeof __VLS_41; }).VListItemSubtitle;
({} as { VListItemSubtitle: typeof __VLS_41; }).VListItemSubtitle;
const __VLS_43 = __VLS_42({ ...{}, class: ("text-disabled mb-1"), }, ...__VLS_functionalComponentArgsRest(__VLS_42));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_41, typeof __VLS_43> & Record<string, unknown>) => void)({ ...{}, class: ("text-disabled mb-1"), });
const __VLS_44 = __VLS_pickFunctionalComponentCtx(__VLS_41, __VLS_43)!;
let __VLS_45!: __VLS_NormalizeEmits<typeof __VLS_44.emit>;
(item.user);
(item.timestamp);
(__VLS_44.slots!).default;
}
{
let __VLS_46!: 'VListItemTitle' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VListItemTitle : (typeof __VLS_resolvedLocalAndGlobalComponents)['VListItemTitle'];
const __VLS_47 = __VLS_asFunctionalComponent(__VLS_46, new __VLS_46({ ...{}, }));
({} as { VListItemTitle: typeof __VLS_46; }).VListItemTitle;
({} as { VListItemTitle: typeof __VLS_46; }).VListItemTitle;
const __VLS_48 = __VLS_47({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_47));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_46, typeof __VLS_48> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_49 = __VLS_pickFunctionalComponentCtx(__VLS_46, __VLS_48)!;
let __VLS_50!: __VLS_NormalizeEmits<typeof __VLS_49.emit>;
(item.action);
(__VLS_49.slots!).default;
}
{
const __VLS_51 = __VLS_intrinsicElements["template"];
const __VLS_52 = __VLS_elementAsFunctionalComponent(__VLS_51);
const __VLS_53 = __VLS_52({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_52));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_51, typeof __VLS_53> & Record<string, unknown>) => void)({ ...{}, });
{
(__VLS_31.slots!).append;
{
let __VLS_54!: 'VListItemAction' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VListItemAction : (typeof __VLS_resolvedLocalAndGlobalComponents)['VListItemAction'];
const __VLS_55 = __VLS_asFunctionalComponent(__VLS_54, new __VLS_54({ ...{}, }));
({} as { VListItemAction: typeof __VLS_54; }).VListItemAction;
({} as { VListItemAction: typeof __VLS_54; }).VListItemAction;
const __VLS_56 = __VLS_55({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_55));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_54, typeof __VLS_56> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_57 = __VLS_pickFunctionalComponentCtx(__VLS_54, __VLS_56)!;
let __VLS_58!: __VLS_NormalizeEmits<typeof __VLS_57.emit>;
{
let __VLS_59!: 'VChip' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VChip : (typeof __VLS_resolvedLocalAndGlobalComponents)['VChip'];
const __VLS_60 = __VLS_asFunctionalComponent(__VLS_59, new __VLS_59({ ...{}, class: ("me-1"), color: ("warning"), }));
({} as { VChip: typeof __VLS_59; }).VChip;
({} as { VChip: typeof __VLS_59; }).VChip;
const __VLS_61 = __VLS_60({ ...{}, class: ("me-1"), color: ("warning"), }, ...__VLS_functionalComponentArgsRest(__VLS_60));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_59, typeof __VLS_61> & Record<string, unknown>) => void)({ ...{}, class: ("me-1"), color: ("warning"), });
const __VLS_62 = __VLS_pickFunctionalComponentCtx(__VLS_59, __VLS_61)!;
let __VLS_63!: __VLS_NormalizeEmits<typeof __VLS_62.emit>;
(item.title);
(__VLS_62.slots!).default;
}
(__VLS_57.slots!).default;
}
}
}
}
}
(__VLS_26.slots!).default;
}
(__VLS_21.slots!).default;
}
}
if (typeof __VLS_styleScopedClasses === 'object' && !Array.isArray(__VLS_styleScopedClasses)) {
__VLS_styleScopedClasses["me-n3"];
__VLS_styleScopedClasses["mt-n2"];
__VLS_styleScopedClasses["card-list"];
__VLS_styleScopedClasses["me-3"];
__VLS_styleScopedClasses["text-disabled"];
__VLS_styleScopedClasses["mb-1"];
__VLS_styleScopedClasses["me-1"];
}
var __VLS_slots!: {};
return __VLS_slots;
}
