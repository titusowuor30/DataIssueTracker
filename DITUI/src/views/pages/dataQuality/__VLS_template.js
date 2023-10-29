import CSVExport from "@/pages/report/CSVExport.vue";
import { __VLS_internalComponent, __VLS_componentsOption, __VLS_name, searchText, applyFilters, perPage, perPageOptions, loadData, facility, facilities, country, countries, exportcsvFileName, exportData, handleCSVExport, selectAll, selectAllRows, filteredDataIssues, selectedRows, action, actions, updateDataIssues, currentPage, totalItems } from "./Datatables.vue";

function __VLS_template() {
let __VLS_ctx!: InstanceType<__VLS_PickNotAny<typeof __VLS_internalComponent, new () => {}>> & {};
/* Components */
let __VLS_otherComponents!: NonNullable<typeof __VLS_internalComponent extends { components: infer C; } ? C : {}> & typeof __VLS_componentsOption;
let __VLS_own!: __VLS_SelfComponent<typeof __VLS_name, typeof __VLS_internalComponent & (new () => { $slots: typeof __VLS_slots; })>;
let __VLS_localComponents!: typeof __VLS_otherComponents & Omit<typeof __VLS_own, keyof typeof __VLS_otherComponents>;
let __VLS_components!: typeof __VLS_localComponents & __VLS_GlobalComponents & typeof __VLS_ctx;
/* Style Scoped */
type __VLS_StyleScopedClasses = {} &
{ 'filters'?: boolean; } &
{ 'filters'?: boolean; } &
{ 'search'?: boolean; } &
{ 'filters'?: boolean; } &
{ 'export-buttons'?: boolean; } &
{ 'filters'?: boolean; } &
{ 'export-buttons'?: boolean; } &
{ 'data-issues-table'?: boolean; } &
{ 'data-issues-table'?: boolean; } &
{ 'data-issues-table'?: boolean; } &
{ 'data-issues-table'?: boolean; } &
{ 'pagination'?: boolean; } &
{ 'pagination'?: boolean; } &
{ 'pagination'?: boolean; };
let __VLS_styleScopedClasses!: __VLS_StyleScopedClasses | keyof __VLS_StyleScopedClasses | (keyof __VLS_StyleScopedClasses)[];
/* CSS variable injection */
/* CSS variable injection end */
let __VLS_resolvedLocalAndGlobalComponents!: {} &
__VLS_WithComponent<'VCard', typeof __VLS_localComponents, "VCard", "VCard", "VCard"> &
__VLS_WithComponent<'VCardTitle', typeof __VLS_localComponents, "VCardTitle", "VCardTitle", "VCardTitle"> &
__VLS_WithComponent<'VRow', typeof __VLS_localComponents, "VRow", "VRow", "VRow"> &
__VLS_WithComponent<'VCol', typeof __VLS_localComponents, "VCol", "VCol", "VCol"> &
__VLS_WithComponent<'VTextField', typeof __VLS_localComponents, "VTextField", "VTextField", "VTextField"> &
__VLS_WithComponent<'VSelect', typeof __VLS_localComponents, "VSelect", "VSelect", "VSelect"> &
__VLS_WithComponent<'VBtn', typeof __VLS_localComponents, "VBtn", "VBtn", "VBtn"> &
__VLS_WithComponent<'CSVExport', typeof __VLS_localComponents, "CSVExport", "CSVExport", "CSVExport"> &
__VLS_WithComponent<'VIcon', typeof __VLS_localComponents, "VIcon", "VIcon", "VIcon"> &
__VLS_WithComponent<'VPagination', typeof __VLS_localComponents, "VPagination", "VPagination", "VPagination">;
__VLS_intrinsicElements.div; __VLS_intrinsicElements.div; __VLS_intrinsicElements.div; __VLS_intrinsicElements.div; __VLS_intrinsicElements.div; __VLS_intrinsicElements.div; __VLS_intrinsicElements.div; __VLS_intrinsicElements.div; __VLS_intrinsicElements.div; __VLS_intrinsicElements.div; __VLS_intrinsicElements.div; __VLS_intrinsicElements.div;
__VLS_components.VCard; __VLS_components.VCard; __VLS_components.VCard; __VLS_components.VCard;
// @ts-ignore
[VCard, VCard, VCard, VCard,];
__VLS_components.VCardTitle; __VLS_components.VCardTitle;
// @ts-ignore
[VCardTitle, VCardTitle,];
__VLS_components.VRow; __VLS_components.VRow; __VLS_components.VRow; __VLS_components.VRow;
// @ts-ignore
[VRow, VRow, VRow, VRow,];
__VLS_components.VCol; __VLS_components.VCol; __VLS_components.VCol; __VLS_components.VCol; __VLS_components.VCol; __VLS_components.VCol; __VLS_components.VCol; __VLS_components.VCol; __VLS_components.VCol; __VLS_components.VCol; __VLS_components.VCol; __VLS_components.VCol; __VLS_components.VCol; __VLS_components.VCol; __VLS_components.VCol; __VLS_components.VCol;
// @ts-ignore
[VCol, VCol, VCol, VCol, VCol, VCol, VCol, VCol, VCol, VCol, VCol, VCol, VCol, VCol, VCol, VCol,];
__VLS_components.VTextField;
// @ts-ignore
[VTextField,];
__VLS_components.VSelect; __VLS_components.VSelect; __VLS_components.VSelect; __VLS_components.VSelect;
// @ts-ignore
[VSelect, VSelect, VSelect, VSelect,];
__VLS_components.VBtn; __VLS_components.VBtn; __VLS_components.VBtn; __VLS_components.VBtn;
// @ts-ignore
[VBtn, VBtn, VBtn, VBtn,];
__VLS_intrinsicElements.i; __VLS_intrinsicElements.i;
__VLS_components.CSVExport;
// @ts-ignore
[CSVExport,];
__VLS_components.VIcon;
// @ts-ignore
[VIcon,];
__VLS_intrinsicElements.table; __VLS_intrinsicElements.table;
__VLS_intrinsicElements.thead; __VLS_intrinsicElements.thead;
__VLS_intrinsicElements.tr; __VLS_intrinsicElements.tr; __VLS_intrinsicElements.tr; __VLS_intrinsicElements.tr;
__VLS_intrinsicElements.th; __VLS_intrinsicElements.th; __VLS_intrinsicElements.th; __VLS_intrinsicElements.th; __VLS_intrinsicElements.th; __VLS_intrinsicElements.th; __VLS_intrinsicElements.th; __VLS_intrinsicElements.th; __VLS_intrinsicElements.th; __VLS_intrinsicElements.th; __VLS_intrinsicElements.th; __VLS_intrinsicElements.th; __VLS_intrinsicElements.th; __VLS_intrinsicElements.th; __VLS_intrinsicElements.th; __VLS_intrinsicElements.th;
__VLS_intrinsicElements.input; __VLS_intrinsicElements.input;
__VLS_intrinsicElements.tbody; __VLS_intrinsicElements.tbody;
__VLS_intrinsicElements.td; __VLS_intrinsicElements.td; __VLS_intrinsicElements.td; __VLS_intrinsicElements.td; __VLS_intrinsicElements.td; __VLS_intrinsicElements.td; __VLS_intrinsicElements.td; __VLS_intrinsicElements.td; __VLS_intrinsicElements.td; __VLS_intrinsicElements.td; __VLS_intrinsicElements.td; __VLS_intrinsicElements.td; __VLS_intrinsicElements.td; __VLS_intrinsicElements.td; __VLS_intrinsicElements.td; __VLS_intrinsicElements.td;
__VLS_intrinsicElements.p; __VLS_intrinsicElements.p;
__VLS_intrinsicElements.span; __VLS_intrinsicElements.span; __VLS_intrinsicElements.span; __VLS_intrinsicElements.span;
__VLS_components.VPagination;
// @ts-ignore
[VPagination,];
{
const __VLS_0 = __VLS_intrinsicElements["div"];
const __VLS_1 = __VLS_elementAsFunctionalComponent(__VLS_0);
const __VLS_2 = __VLS_1({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_1));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_0, typeof __VLS_2> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_3 = __VLS_pickFunctionalComponentCtx(__VLS_0, __VLS_2)!;
let __VLS_4!: __VLS_NormalizeEmits<typeof __VLS_3.emit>;
{
let __VLS_5!: 'VCard' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VCard : (typeof __VLS_resolvedLocalAndGlobalComponents)['VCard'];
const __VLS_6 = __VLS_asFunctionalComponent(__VLS_5, new __VLS_5({ ...{}, }));
({} as { VCard: typeof __VLS_5; }).VCard;
({} as { VCard: typeof __VLS_5; }).VCard;
const __VLS_7 = __VLS_6({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_6));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_5, typeof __VLS_7> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_8 = __VLS_pickFunctionalComponentCtx(__VLS_5, __VLS_7)!;
let __VLS_9!: __VLS_NormalizeEmits<typeof __VLS_8.emit>;
{
let __VLS_10!: 'VCardTitle' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VCardTitle : (typeof __VLS_resolvedLocalAndGlobalComponents)['VCardTitle'];
const __VLS_11 = __VLS_asFunctionalComponent(__VLS_10, new __VLS_10({ ...{}, }));
({} as { VCardTitle: typeof __VLS_10; }).VCardTitle;
({} as { VCardTitle: typeof __VLS_10; }).VCardTitle;
const __VLS_12 = __VLS_11({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_11));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_10, typeof __VLS_12> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_13 = __VLS_pickFunctionalComponentCtx(__VLS_10, __VLS_12)!;
let __VLS_14!: __VLS_NormalizeEmits<typeof __VLS_13.emit>;
{
let __VLS_15!: 'VRow' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VRow : (typeof __VLS_resolvedLocalAndGlobalComponents)['VRow'];
const __VLS_16 = __VLS_asFunctionalComponent(__VLS_15, new __VLS_15({ ...{}, style: ({}), align: ("center"), justify: ("space-between"), class: ("px-2 m-0"), }));
({} as { VRow: typeof __VLS_15; }).VRow;
({} as { VRow: typeof __VLS_15; }).VRow;
const __VLS_17 = __VLS_16({ ...{}, style: ({}), align: ("center"), justify: ("space-between"), class: ("px-2 m-0"), }, ...__VLS_functionalComponentArgsRest(__VLS_16));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_15, typeof __VLS_17> & Record<string, unknown>) => void)({ ...{}, style: ({}), align: ("center"), justify: ("space-between"), class: ("px-2 m-0"), });
const __VLS_18 = __VLS_pickFunctionalComponentCtx(__VLS_15, __VLS_17)!;
let __VLS_19!: __VLS_NormalizeEmits<typeof __VLS_18.emit>;
{
let __VLS_20!: 'VCol' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VCol : (typeof __VLS_resolvedLocalAndGlobalComponents)['VCol'];
const __VLS_21 = __VLS_asFunctionalComponent(__VLS_20, new __VLS_20({ ...{}, cols: ("3"), }));
({} as { VCol: typeof __VLS_20; }).VCol;
({} as { VCol: typeof __VLS_20; }).VCol;
const __VLS_22 = __VLS_21({ ...{}, cols: ("3"), }, ...__VLS_functionalComponentArgsRest(__VLS_21));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_20, typeof __VLS_22> & Record<string, unknown>) => void)({ ...{}, cols: ("3"), });
const __VLS_23 = __VLS_pickFunctionalComponentCtx(__VLS_20, __VLS_22)!;
let __VLS_24!: __VLS_NormalizeEmits<typeof __VLS_23.emit>;
{
let __VLS_25!: 'VTextField' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VTextField : (typeof __VLS_resolvedLocalAndGlobalComponents)['VTextField'];
const __VLS_26 = __VLS_asFunctionalComponent(__VLS_25, new __VLS_25({ ...{ onInput: {} as any, }, modelValue: ((__VLS_ctx.searchText)), placeholder: ("Search Patient ID, Date, or Status"), label: ("Search"), outlined: (true), dense: (true), }));
({} as { VTextField: typeof __VLS_25; }).VTextField;
const __VLS_27 = __VLS_26({ ...{ onInput: {} as any, }, modelValue: ((__VLS_ctx.searchText)), placeholder: ("Search Patient ID, Date, or Status"), label: ("Search"), outlined: (true), dense: (true), }, ...__VLS_functionalComponentArgsRest(__VLS_26));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_25, typeof __VLS_27> & Record<string, unknown>) => void)({ ...{ onInput: {} as any, }, modelValue: ((__VLS_ctx.searchText)), placeholder: ("Search Patient ID, Date, or Status"), label: ("Search"), outlined: (true), dense: (true), });
const __VLS_28 = __VLS_pickFunctionalComponentCtx(__VLS_25, __VLS_27)!;
let __VLS_29!: __VLS_NormalizeEmits<typeof __VLS_28.emit>;
let __VLS_30 = { 'input': __VLS_pickEvent(__VLS_29['input'], ({} as __VLS_FunctionalComponentProps<typeof __VLS_26, typeof __VLS_27>).onInput) };
__VLS_30 = { input: (__VLS_ctx.applyFilters) };
}
(__VLS_23.slots!).default;
}
{
let __VLS_31!: 'VCol' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VCol : (typeof __VLS_resolvedLocalAndGlobalComponents)['VCol'];
const __VLS_32 = __VLS_asFunctionalComponent(__VLS_31, new __VLS_31({ ...{}, cols: ("2"), }));
({} as { VCol: typeof __VLS_31; }).VCol;
({} as { VCol: typeof __VLS_31; }).VCol;
const __VLS_33 = __VLS_32({ ...{}, cols: ("2"), }, ...__VLS_functionalComponentArgsRest(__VLS_32));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_31, typeof __VLS_33> & Record<string, unknown>) => void)({ ...{}, cols: ("2"), });
const __VLS_34 = __VLS_pickFunctionalComponentCtx(__VLS_31, __VLS_33)!;
let __VLS_35!: __VLS_NormalizeEmits<typeof __VLS_34.emit>;
{
const __VLS_36 = __VLS_intrinsicElements["div"];
const __VLS_37 = __VLS_elementAsFunctionalComponent(__VLS_36);
const __VLS_38 = __VLS_37({ ...{}, class: ("select-per-page"), }, ...__VLS_functionalComponentArgsRest(__VLS_37));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_36, typeof __VLS_38> & Record<string, unknown>) => void)({ ...{}, class: ("select-per-page"), });
const __VLS_39 = __VLS_pickFunctionalComponentCtx(__VLS_36, __VLS_38)!;
let __VLS_40!: __VLS_NormalizeEmits<typeof __VLS_39.emit>;
{
let __VLS_41!: 'VSelect' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VSelect : (typeof __VLS_resolvedLocalAndGlobalComponents)['VSelect'];
const __VLS_42 = __VLS_asFunctionalComponent(__VLS_41, new __VLS_41({ ...{ onClick: {} as any, }, modelValue: ((__VLS_ctx.perPage)), items: ((__VLS_ctx.perPageOptions)), label: ("Records Per Page"), }));
({} as { VSelect: typeof __VLS_41; }).VSelect;
const __VLS_43 = __VLS_42({ ...{ onClick: {} as any, }, modelValue: ((__VLS_ctx.perPage)), items: ((__VLS_ctx.perPageOptions)), label: ("Records Per Page"), }, ...__VLS_functionalComponentArgsRest(__VLS_42));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_41, typeof __VLS_43> & Record<string, unknown>) => void)({ ...{ onClick: {} as any, }, modelValue: ((__VLS_ctx.perPage)), items: ((__VLS_ctx.perPageOptions)), label: ("Records Per Page"), });
const __VLS_44 = __VLS_pickFunctionalComponentCtx(__VLS_41, __VLS_43)!;
let __VLS_45!: __VLS_NormalizeEmits<typeof __VLS_44.emit>;
let __VLS_46 = { 'click': __VLS_pickEvent(__VLS_45['click'], ({} as __VLS_FunctionalComponentProps<typeof __VLS_42, typeof __VLS_43>).onClick) };
__VLS_46 = { click: (__VLS_ctx.loadData) };
}
(__VLS_39.slots!).default;
}
(__VLS_34.slots!).default;
}
{
let __VLS_47!: 'VCol' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VCol : (typeof __VLS_resolvedLocalAndGlobalComponents)['VCol'];
const __VLS_48 = __VLS_asFunctionalComponent(__VLS_47, new __VLS_47({ ...{}, cols: ("2"), }));
({} as { VCol: typeof __VLS_47; }).VCol;
({} as { VCol: typeof __VLS_47; }).VCol;
const __VLS_49 = __VLS_48({ ...{}, cols: ("2"), }, ...__VLS_functionalComponentArgsRest(__VLS_48));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_47, typeof __VLS_49> & Record<string, unknown>) => void)({ ...{}, cols: ("2"), });
const __VLS_50 = __VLS_pickFunctionalComponentCtx(__VLS_47, __VLS_49)!;
let __VLS_51!: __VLS_NormalizeEmits<typeof __VLS_50.emit>;
{
const __VLS_52 = __VLS_intrinsicElements["div"];
const __VLS_53 = __VLS_elementAsFunctionalComponent(__VLS_52);
const __VLS_54 = __VLS_53({ ...{}, class: ("select-per-page"), }, ...__VLS_functionalComponentArgsRest(__VLS_53));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_52, typeof __VLS_54> & Record<string, unknown>) => void)({ ...{}, class: ("select-per-page"), });
const __VLS_55 = __VLS_pickFunctionalComponentCtx(__VLS_52, __VLS_54)!;
let __VLS_56!: __VLS_NormalizeEmits<typeof __VLS_55.emit>;
{
let __VLS_57!: 'VSelect' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VSelect : (typeof __VLS_resolvedLocalAndGlobalComponents)['VSelect'];
const __VLS_58 = __VLS_asFunctionalComponent(__VLS_57, new __VLS_57({ ...{ onClick: {} as any, }, modelValue: ((__VLS_ctx.facility)), items: ((__VLS_ctx.facilities)), label: ("Select Facility"), }));
({} as { VSelect: typeof __VLS_57; }).VSelect;
const __VLS_59 = __VLS_58({ ...{ onClick: {} as any, }, modelValue: ((__VLS_ctx.facility)), items: ((__VLS_ctx.facilities)), label: ("Select Facility"), }, ...__VLS_functionalComponentArgsRest(__VLS_58));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_57, typeof __VLS_59> & Record<string, unknown>) => void)({ ...{ onClick: {} as any, }, modelValue: ((__VLS_ctx.facility)), items: ((__VLS_ctx.facilities)), label: ("Select Facility"), });
const __VLS_60 = __VLS_pickFunctionalComponentCtx(__VLS_57, __VLS_59)!;
let __VLS_61!: __VLS_NormalizeEmits<typeof __VLS_60.emit>;
let __VLS_62 = { 'click': __VLS_pickEvent(__VLS_61['click'], ({} as __VLS_FunctionalComponentProps<typeof __VLS_58, typeof __VLS_59>).onClick) };
__VLS_62 = { click: (__VLS_ctx.loadData) };
}
(__VLS_55.slots!).default;
}
(__VLS_50.slots!).default;
}
{
let __VLS_63!: 'VCol' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VCol : (typeof __VLS_resolvedLocalAndGlobalComponents)['VCol'];
const __VLS_64 = __VLS_asFunctionalComponent(__VLS_63, new __VLS_63({ ...{}, cols: ("2"), }));
({} as { VCol: typeof __VLS_63; }).VCol;
({} as { VCol: typeof __VLS_63; }).VCol;
const __VLS_65 = __VLS_64({ ...{}, cols: ("2"), }, ...__VLS_functionalComponentArgsRest(__VLS_64));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_63, typeof __VLS_65> & Record<string, unknown>) => void)({ ...{}, cols: ("2"), });
const __VLS_66 = __VLS_pickFunctionalComponentCtx(__VLS_63, __VLS_65)!;
let __VLS_67!: __VLS_NormalizeEmits<typeof __VLS_66.emit>;
{
const __VLS_68 = __VLS_intrinsicElements["div"];
const __VLS_69 = __VLS_elementAsFunctionalComponent(__VLS_68);
const __VLS_70 = __VLS_69({ ...{}, class: ("select-per-page"), }, ...__VLS_functionalComponentArgsRest(__VLS_69));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_68, typeof __VLS_70> & Record<string, unknown>) => void)({ ...{}, class: ("select-per-page"), });
const __VLS_71 = __VLS_pickFunctionalComponentCtx(__VLS_68, __VLS_70)!;
let __VLS_72!: __VLS_NormalizeEmits<typeof __VLS_71.emit>;
{
let __VLS_73!: 'VSelect' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VSelect : (typeof __VLS_resolvedLocalAndGlobalComponents)['VSelect'];
const __VLS_74 = __VLS_asFunctionalComponent(__VLS_73, new __VLS_73({ ...{ onClick: {} as any, }, modelValue: ((__VLS_ctx.country)), items: ((__VLS_ctx.countries)), label: ("Select Country"), }));
({} as { VSelect: typeof __VLS_73; }).VSelect;
const __VLS_75 = __VLS_74({ ...{ onClick: {} as any, }, modelValue: ((__VLS_ctx.country)), items: ((__VLS_ctx.countries)), label: ("Select Country"), }, ...__VLS_functionalComponentArgsRest(__VLS_74));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_73, typeof __VLS_75> & Record<string, unknown>) => void)({ ...{ onClick: {} as any, }, modelValue: ((__VLS_ctx.country)), items: ((__VLS_ctx.countries)), label: ("Select Country"), });
const __VLS_76 = __VLS_pickFunctionalComponentCtx(__VLS_73, __VLS_75)!;
let __VLS_77!: __VLS_NormalizeEmits<typeof __VLS_76.emit>;
let __VLS_78 = { 'click': __VLS_pickEvent(__VLS_77['click'], ({} as __VLS_FunctionalComponentProps<typeof __VLS_74, typeof __VLS_75>).onClick) };
__VLS_78 = { click: (__VLS_ctx.loadData) };
}
(__VLS_71.slots!).default;
}
(__VLS_66.slots!).default;
}
{
let __VLS_79!: 'VCol' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VCol : (typeof __VLS_resolvedLocalAndGlobalComponents)['VCol'];
const __VLS_80 = __VLS_asFunctionalComponent(__VLS_79, new __VLS_79({ ...{}, cols: ("1"), class: ("text-right"), }));
({} as { VCol: typeof __VLS_79; }).VCol;
({} as { VCol: typeof __VLS_79; }).VCol;
const __VLS_81 = __VLS_80({ ...{}, cols: ("1"), class: ("text-right"), }, ...__VLS_functionalComponentArgsRest(__VLS_80));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_79, typeof __VLS_81> & Record<string, unknown>) => void)({ ...{}, cols: ("1"), class: ("text-right"), });
const __VLS_82 = __VLS_pickFunctionalComponentCtx(__VLS_79, __VLS_81)!;
let __VLS_83!: __VLS_NormalizeEmits<typeof __VLS_82.emit>;
{
let __VLS_84!: 'VBtn' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VBtn : (typeof __VLS_resolvedLocalAndGlobalComponents)['VBtn'];
const __VLS_85 = __VLS_asFunctionalComponent(__VLS_84, new __VLS_84({ ...{ onClick: {} as any, }, class: ("m-auto"), }));
({} as { VBtn: typeof __VLS_84; }).VBtn;
({} as { VBtn: typeof __VLS_84; }).VBtn;
const __VLS_86 = __VLS_85({ ...{ onClick: {} as any, }, class: ("m-auto"), }, ...__VLS_functionalComponentArgsRest(__VLS_85));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_84, typeof __VLS_86> & Record<string, unknown>) => void)({ ...{ onClick: {} as any, }, class: ("m-auto"), });
const __VLS_87 = __VLS_pickFunctionalComponentCtx(__VLS_84, __VLS_86)!;
let __VLS_88!: __VLS_NormalizeEmits<typeof __VLS_87.emit>;
let __VLS_89 = { 'click': __VLS_pickEvent(__VLS_88['click'], ({} as __VLS_FunctionalComponentProps<typeof __VLS_85, typeof __VLS_86>).onClick) };
__VLS_89 = { click: (__VLS_ctx.loadData) };
{
const __VLS_90 = __VLS_intrinsicElements["i"];
const __VLS_91 = __VLS_elementAsFunctionalComponent(__VLS_90);
const __VLS_92 = __VLS_91({ ...{}, class: ("uil uil-search"), }, ...__VLS_functionalComponentArgsRest(__VLS_91));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_90, typeof __VLS_92> & Record<string, unknown>) => void)({ ...{}, class: ("uil uil-search"), });
const __VLS_93 = __VLS_pickFunctionalComponentCtx(__VLS_90, __VLS_92)!;
let __VLS_94!: __VLS_NormalizeEmits<typeof __VLS_93.emit>;
}
(__VLS_87.slots!).default;
}
(__VLS_82.slots!).default;
}
{
let __VLS_95!: 'VCol' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VCol : (typeof __VLS_resolvedLocalAndGlobalComponents)['VCol'];
const __VLS_96 = __VLS_asFunctionalComponent(__VLS_95, new __VLS_95({ ...{}, cols: ("2"), class: ("text-right"), }));
({} as { VCol: typeof __VLS_95; }).VCol;
({} as { VCol: typeof __VLS_95; }).VCol;
const __VLS_97 = __VLS_96({ ...{}, cols: ("2"), class: ("text-right"), }, ...__VLS_functionalComponentArgsRest(__VLS_96));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_95, typeof __VLS_97> & Record<string, unknown>) => void)({ ...{}, cols: ("2"), class: ("text-right"), });
const __VLS_98 = __VLS_pickFunctionalComponentCtx(__VLS_95, __VLS_97)!;
let __VLS_99!: __VLS_NormalizeEmits<typeof __VLS_98.emit>;
{
let __VLS_100!: 'CSVExport' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.CSVExport : (typeof __VLS_resolvedLocalAndGlobalComponents)['CSVExport'];
const __VLS_101 = __VLS_asFunctionalComponent(__VLS_100, new __VLS_100({ ...{ onExportCsv: {} as any, }, filename: ((__VLS_ctx.exportcsvFileName)), data: ((__VLS_ctx.exportData)), }));
({} as { CSVExport: typeof __VLS_100; }).CSVExport;
const __VLS_102 = __VLS_101({ ...{ onExportCsv: {} as any, }, filename: ((__VLS_ctx.exportcsvFileName)), data: ((__VLS_ctx.exportData)), }, ...__VLS_functionalComponentArgsRest(__VLS_101));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_100, typeof __VLS_102> & Record<string, unknown>) => void)({ ...{ onExportCsv: {} as any, }, filename: ((__VLS_ctx.exportcsvFileName)), data: ((__VLS_ctx.exportData)), });
const __VLS_103 = __VLS_pickFunctionalComponentCtx(__VLS_100, __VLS_102)!;
let __VLS_104!: __VLS_NormalizeEmits<typeof __VLS_103.emit>;
let __VLS_105 = { 'export-csv': __VLS_pickEvent(__VLS_104['export-csv'], ({} as __VLS_FunctionalComponentProps<typeof __VLS_101, typeof __VLS_102>).onExportCsv) };
__VLS_105 = { "export-csv": (__VLS_ctx.handleCSVExport) };
}
{
let __VLS_106!: 'VIcon' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VIcon : (typeof __VLS_resolvedLocalAndGlobalComponents)['VIcon'];
const __VLS_107 = __VLS_asFunctionalComponent(__VLS_106, new __VLS_106({ ...{}, size: ("40"), icon: ("bxs-file-pdf"), class: ("text-error"), }));
({} as { VIcon: typeof __VLS_106; }).VIcon;
const __VLS_108 = __VLS_107({ ...{}, size: ("40"), icon: ("bxs-file-pdf"), class: ("text-error"), }, ...__VLS_functionalComponentArgsRest(__VLS_107));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_106, typeof __VLS_108> & Record<string, unknown>) => void)({ ...{}, size: ("40"), icon: ("bxs-file-pdf"), class: ("text-error"), });
const __VLS_109 = __VLS_pickFunctionalComponentCtx(__VLS_106, __VLS_108)!;
let __VLS_110!: __VLS_NormalizeEmits<typeof __VLS_109.emit>;
}
(__VLS_98.slots!).default;
}
(__VLS_18.slots!).default;
}
(__VLS_13.slots!).default;
}
{
const __VLS_111 = __VLS_intrinsicElements["table"];
const __VLS_112 = __VLS_elementAsFunctionalComponent(__VLS_111);
const __VLS_113 = __VLS_112({ ...{}, class: ("data-issues-table"), }, ...__VLS_functionalComponentArgsRest(__VLS_112));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_111, typeof __VLS_113> & Record<string, unknown>) => void)({ ...{}, class: ("data-issues-table"), });
const __VLS_114 = __VLS_pickFunctionalComponentCtx(__VLS_111, __VLS_113)!;
let __VLS_115!: __VLS_NormalizeEmits<typeof __VLS_114.emit>;
{
const __VLS_116 = __VLS_intrinsicElements["thead"];
const __VLS_117 = __VLS_elementAsFunctionalComponent(__VLS_116);
const __VLS_118 = __VLS_117({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_117));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_116, typeof __VLS_118> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_119 = __VLS_pickFunctionalComponentCtx(__VLS_116, __VLS_118)!;
let __VLS_120!: __VLS_NormalizeEmits<typeof __VLS_119.emit>;
{
const __VLS_121 = __VLS_intrinsicElements["tr"];
const __VLS_122 = __VLS_elementAsFunctionalComponent(__VLS_121);
const __VLS_123 = __VLS_122({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_122));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_121, typeof __VLS_123> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_124 = __VLS_pickFunctionalComponentCtx(__VLS_121, __VLS_123)!;
let __VLS_125!: __VLS_NormalizeEmits<typeof __VLS_124.emit>;
{
const __VLS_126 = __VLS_intrinsicElements["th"];
const __VLS_127 = __VLS_elementAsFunctionalComponent(__VLS_126);
const __VLS_128 = __VLS_127({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_127));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_126, typeof __VLS_128> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_129 = __VLS_pickFunctionalComponentCtx(__VLS_126, __VLS_128)!;
let __VLS_130!: __VLS_NormalizeEmits<typeof __VLS_129.emit>;
{
const __VLS_131 = __VLS_intrinsicElements["input"];
const __VLS_132 = __VLS_elementAsFunctionalComponent(__VLS_131);
const __VLS_133 = __VLS_132({ ...{ onChange: {} as any, }, type: ("checkbox"), }, ...__VLS_functionalComponentArgsRest(__VLS_132));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_131, typeof __VLS_133> & Record<string, unknown>) => void)({ ...{ onChange: {} as any, }, type: ("checkbox"), });
const __VLS_134 = __VLS_pickFunctionalComponentCtx(__VLS_131, __VLS_133)!;
let __VLS_135!: __VLS_NormalizeEmits<typeof __VLS_134.emit>;
(__VLS_ctx.selectAll);
let __VLS_136 = { 'change': __VLS_pickEvent(__VLS_135['change'], ({} as __VLS_FunctionalComponentProps<typeof __VLS_132, typeof __VLS_133>).onChange) };
__VLS_136 = { change: (__VLS_ctx.selectAllRows) };
}
(__VLS_129.slots!).default;
}
{
const __VLS_137 = __VLS_intrinsicElements["th"];
const __VLS_138 = __VLS_elementAsFunctionalComponent(__VLS_137);
const __VLS_139 = __VLS_138({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_138));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_137, typeof __VLS_139> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_140 = __VLS_pickFunctionalComponentCtx(__VLS_137, __VLS_139)!;
let __VLS_141!: __VLS_NormalizeEmits<typeof __VLS_140.emit>;
(__VLS_140.slots!).default;
}
{
const __VLS_142 = __VLS_intrinsicElements["th"];
const __VLS_143 = __VLS_elementAsFunctionalComponent(__VLS_142);
const __VLS_144 = __VLS_143({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_143));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_142, typeof __VLS_144> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_145 = __VLS_pickFunctionalComponentCtx(__VLS_142, __VLS_144)!;
let __VLS_146!: __VLS_NormalizeEmits<typeof __VLS_145.emit>;
(__VLS_145.slots!).default;
}
{
const __VLS_147 = __VLS_intrinsicElements["th"];
const __VLS_148 = __VLS_elementAsFunctionalComponent(__VLS_147);
const __VLS_149 = __VLS_148({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_148));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_147, typeof __VLS_149> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_150 = __VLS_pickFunctionalComponentCtx(__VLS_147, __VLS_149)!;
let __VLS_151!: __VLS_NormalizeEmits<typeof __VLS_150.emit>;
(__VLS_150.slots!).default;
}
{
const __VLS_152 = __VLS_intrinsicElements["th"];
const __VLS_153 = __VLS_elementAsFunctionalComponent(__VLS_152);
const __VLS_154 = __VLS_153({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_153));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_152, typeof __VLS_154> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_155 = __VLS_pickFunctionalComponentCtx(__VLS_152, __VLS_154)!;
let __VLS_156!: __VLS_NormalizeEmits<typeof __VLS_155.emit>;
(__VLS_155.slots!).default;
}
{
const __VLS_157 = __VLS_intrinsicElements["th"];
const __VLS_158 = __VLS_elementAsFunctionalComponent(__VLS_157);
const __VLS_159 = __VLS_158({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_158));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_157, typeof __VLS_159> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_160 = __VLS_pickFunctionalComponentCtx(__VLS_157, __VLS_159)!;
let __VLS_161!: __VLS_NormalizeEmits<typeof __VLS_160.emit>;
(__VLS_160.slots!).default;
}
{
const __VLS_162 = __VLS_intrinsicElements["th"];
const __VLS_163 = __VLS_elementAsFunctionalComponent(__VLS_162);
const __VLS_164 = __VLS_163({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_163));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_162, typeof __VLS_164> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_165 = __VLS_pickFunctionalComponentCtx(__VLS_162, __VLS_164)!;
let __VLS_166!: __VLS_NormalizeEmits<typeof __VLS_165.emit>;
(__VLS_165.slots!).default;
}
{
const __VLS_167 = __VLS_intrinsicElements["th"];
const __VLS_168 = __VLS_elementAsFunctionalComponent(__VLS_167);
const __VLS_169 = __VLS_168({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_168));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_167, typeof __VLS_169> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_170 = __VLS_pickFunctionalComponentCtx(__VLS_167, __VLS_169)!;
let __VLS_171!: __VLS_NormalizeEmits<typeof __VLS_170.emit>;
(__VLS_170.slots!).default;
}
(__VLS_124.slots!).default;
}
(__VLS_119.slots!).default;
}
{
const __VLS_172 = __VLS_intrinsicElements["tbody"];
const __VLS_173 = __VLS_elementAsFunctionalComponent(__VLS_172);
const __VLS_174 = __VLS_173({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_173));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_172, typeof __VLS_174> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_175 = __VLS_pickFunctionalComponentCtx(__VLS_172, __VLS_174)!;
let __VLS_176!: __VLS_NormalizeEmits<typeof __VLS_175.emit>;
for (const [issue] of __VLS_getVForSourceType((__VLS_ctx.filteredDataIssues)!)) {
{
const __VLS_177 = __VLS_intrinsicElements["tr"];
const __VLS_178 = __VLS_elementAsFunctionalComponent(__VLS_177);
const __VLS_179 = __VLS_178({ ...{}, key: ((issue.id)), }, ...__VLS_functionalComponentArgsRest(__VLS_178));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_177, typeof __VLS_179> & Record<string, unknown>) => void)({ ...{}, key: ((issue.id)), });
const __VLS_180 = __VLS_pickFunctionalComponentCtx(__VLS_177, __VLS_179)!;
let __VLS_181!: __VLS_NormalizeEmits<typeof __VLS_180.emit>;
{
const __VLS_182 = __VLS_intrinsicElements["td"];
const __VLS_183 = __VLS_elementAsFunctionalComponent(__VLS_182);
const __VLS_184 = __VLS_183({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_183));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_182, typeof __VLS_184> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_185 = __VLS_pickFunctionalComponentCtx(__VLS_182, __VLS_184)!;
let __VLS_186!: __VLS_NormalizeEmits<typeof __VLS_185.emit>;
{
const __VLS_187 = __VLS_intrinsicElements["input"];
const __VLS_188 = __VLS_elementAsFunctionalComponent(__VLS_187);
const __VLS_189 = __VLS_188({ ...{}, type: ("checkbox"), value: ((issue.id)), }, ...__VLS_functionalComponentArgsRest(__VLS_188));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_187, typeof __VLS_189> & Record<string, unknown>) => void)({ ...{}, type: ("checkbox"), value: ((issue.id)), });
const __VLS_190 = __VLS_pickFunctionalComponentCtx(__VLS_187, __VLS_189)!;
let __VLS_191!: __VLS_NormalizeEmits<typeof __VLS_190.emit>;
(__VLS_ctx.selectedRows);
}
(__VLS_185.slots!).default;
}
{
const __VLS_192 = __VLS_intrinsicElements["td"];
const __VLS_193 = __VLS_elementAsFunctionalComponent(__VLS_192);
const __VLS_194 = __VLS_193({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_193));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_192, typeof __VLS_194> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_195 = __VLS_pickFunctionalComponentCtx(__VLS_192, __VLS_194)!;
let __VLS_196!: __VLS_NormalizeEmits<typeof __VLS_195.emit>;
(issue.id);
(__VLS_195.slots!).default;
}
{
const __VLS_197 = __VLS_intrinsicElements["td"];
const __VLS_198 = __VLS_elementAsFunctionalComponent(__VLS_197);
const __VLS_199 = __VLS_198({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_198));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_197, typeof __VLS_199> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_200 = __VLS_pickFunctionalComponentCtx(__VLS_197, __VLS_199)!;
let __VLS_201!: __VLS_NormalizeEmits<typeof __VLS_200.emit>;
(issue.country);
(__VLS_200.slots!).default;
}
{
const __VLS_202 = __VLS_intrinsicElements["td"];
const __VLS_203 = __VLS_elementAsFunctionalComponent(__VLS_202);
const __VLS_204 = __VLS_203({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_203));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_202, typeof __VLS_204> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_205 = __VLS_pickFunctionalComponentCtx(__VLS_202, __VLS_204)!;
let __VLS_206!: __VLS_NormalizeEmits<typeof __VLS_205.emit>;
(issue.facility_name);
(__VLS_205.slots!).default;
}
{
const __VLS_207 = __VLS_intrinsicElements["td"];
const __VLS_208 = __VLS_elementAsFunctionalComponent(__VLS_207);
const __VLS_209 = __VLS_208({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_208));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_207, typeof __VLS_209> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_210 = __VLS_pickFunctionalComponentCtx(__VLS_207, __VLS_209)!;
let __VLS_211!: __VLS_NormalizeEmits<typeof __VLS_210.emit>;
(issue.patient_id);
(__VLS_210.slots!).default;
}
{
const __VLS_212 = __VLS_intrinsicElements["td"];
const __VLS_213 = __VLS_elementAsFunctionalComponent(__VLS_212);
const __VLS_214 = __VLS_213({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_213));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_212, typeof __VLS_214> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_215 = __VLS_pickFunctionalComponentCtx(__VLS_212, __VLS_214)!;
let __VLS_216!: __VLS_NormalizeEmits<typeof __VLS_215.emit>;
(issue.date_of_entry);
(__VLS_215.slots!).default;
}
{
const __VLS_217 = __VLS_intrinsicElements["td"];
const __VLS_218 = __VLS_elementAsFunctionalComponent(__VLS_217);
const __VLS_219 = __VLS_218({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_218));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_217, typeof __VLS_219> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_220 = __VLS_pickFunctionalComponentCtx(__VLS_217, __VLS_219)!;
let __VLS_221!: __VLS_NormalizeEmits<typeof __VLS_220.emit>;
(issue.inconsistency);
(__VLS_220.slots!).default;
}
{
const __VLS_222 = __VLS_intrinsicElements["td"];
const __VLS_223 = __VLS_elementAsFunctionalComponent(__VLS_222);
const __VLS_224 = __VLS_223({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_223));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_222, typeof __VLS_224> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_225 = __VLS_pickFunctionalComponentCtx(__VLS_222, __VLS_224)!;
let __VLS_226!: __VLS_NormalizeEmits<typeof __VLS_225.emit>;
(issue.action_taken);
(__VLS_225.slots!).default;
}
(__VLS_180.slots!).default;
}
// @ts-ignore
[searchText, searchText, searchText, applyFilters, perPage, perPageOptions, perPage, perPageOptions, perPage, perPageOptions, loadData, facility, facilities, facility, facilities, facility, facilities, loadData, country, countries, country, countries, country, countries, loadData, loadData, exportcsvFileName, exportData, exportcsvFileName, exportData, exportcsvFileName, exportData, handleCSVExport, selectAll, selectAllRows, filteredDataIssues, selectedRows,];
}
(__VLS_175.slots!).default;
}
(__VLS_114.slots!).default;
}
if (__VLS_ctx.filteredDataIssues.length === 0) {
{
const __VLS_227 = __VLS_intrinsicElements["p"];
const __VLS_228 = __VLS_elementAsFunctionalComponent(__VLS_227);
const __VLS_229 = __VLS_228({ ...{}, class: ("text-muted px-2"), }, ...__VLS_functionalComponentArgsRest(__VLS_228));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_227, typeof __VLS_229> & Record<string, unknown>) => void)({ ...{}, class: ("text-muted px-2"), });
const __VLS_230 = __VLS_pickFunctionalComponentCtx(__VLS_227, __VLS_229)!;
let __VLS_231!: __VLS_NormalizeEmits<typeof __VLS_230.emit>;
(__VLS_230.slots!).default;
}
// @ts-ignore
[filteredDataIssues,];
}
{
let __VLS_232!: 'VCard' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VCard : (typeof __VLS_resolvedLocalAndGlobalComponents)['VCard'];
const __VLS_233 = __VLS_asFunctionalComponent(__VLS_232, new __VLS_232({ ...{}, class: ("px-2 py-2"), }));
({} as { VCard: typeof __VLS_232; }).VCard;
({} as { VCard: typeof __VLS_232; }).VCard;
const __VLS_234 = __VLS_233({ ...{}, class: ("px-2 py-2"), }, ...__VLS_functionalComponentArgsRest(__VLS_233));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_232, typeof __VLS_234> & Record<string, unknown>) => void)({ ...{}, class: ("px-2 py-2"), });
const __VLS_235 = __VLS_pickFunctionalComponentCtx(__VLS_232, __VLS_234)!;
let __VLS_236!: __VLS_NormalizeEmits<typeof __VLS_235.emit>;
{
let __VLS_237!: 'VRow' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VRow : (typeof __VLS_resolvedLocalAndGlobalComponents)['VRow'];
const __VLS_238 = __VLS_asFunctionalComponent(__VLS_237, new __VLS_237({ ...{}, }));
({} as { VRow: typeof __VLS_237; }).VRow;
({} as { VRow: typeof __VLS_237; }).VRow;
const __VLS_239 = __VLS_238({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_238));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_237, typeof __VLS_239> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_240 = __VLS_pickFunctionalComponentCtx(__VLS_237, __VLS_239)!;
let __VLS_241!: __VLS_NormalizeEmits<typeof __VLS_240.emit>;
{
let __VLS_242!: 'VCol' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VCol : (typeof __VLS_resolvedLocalAndGlobalComponents)['VCol'];
const __VLS_243 = __VLS_asFunctionalComponent(__VLS_242, new __VLS_242({ ...{}, cols: ("3"), }));
({} as { VCol: typeof __VLS_242; }).VCol;
({} as { VCol: typeof __VLS_242; }).VCol;
const __VLS_244 = __VLS_243({ ...{}, cols: ("3"), }, ...__VLS_functionalComponentArgsRest(__VLS_243));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_242, typeof __VLS_244> & Record<string, unknown>) => void)({ ...{}, cols: ("3"), });
const __VLS_245 = __VLS_pickFunctionalComponentCtx(__VLS_242, __VLS_244)!;
let __VLS_246!: __VLS_NormalizeEmits<typeof __VLS_245.emit>;
{
const __VLS_247 = __VLS_intrinsicElements["div"];
const __VLS_248 = __VLS_elementAsFunctionalComponent(__VLS_247);
const __VLS_249 = __VLS_248({ ...{}, class: ("select-action"), }, ...__VLS_functionalComponentArgsRest(__VLS_248));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_247, typeof __VLS_249> & Record<string, unknown>) => void)({ ...{}, class: ("select-action"), });
const __VLS_250 = __VLS_pickFunctionalComponentCtx(__VLS_247, __VLS_249)!;
let __VLS_251!: __VLS_NormalizeEmits<typeof __VLS_250.emit>;
{
let __VLS_252!: 'VSelect' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VSelect : (typeof __VLS_resolvedLocalAndGlobalComponents)['VSelect'];
const __VLS_253 = __VLS_asFunctionalComponent(__VLS_252, new __VLS_252({ ...{}, modelValue: ((__VLS_ctx.action)), items: ((__VLS_ctx.actions)), label: ("Select Action"), }));
({} as { VSelect: typeof __VLS_252; }).VSelect;
const __VLS_254 = __VLS_253({ ...{}, modelValue: ((__VLS_ctx.action)), items: ((__VLS_ctx.actions)), label: ("Select Action"), }, ...__VLS_functionalComponentArgsRest(__VLS_253));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_252, typeof __VLS_254> & Record<string, unknown>) => void)({ ...{}, modelValue: ((__VLS_ctx.action)), items: ((__VLS_ctx.actions)), label: ("Select Action"), });
const __VLS_255 = __VLS_pickFunctionalComponentCtx(__VLS_252, __VLS_254)!;
let __VLS_256!: __VLS_NormalizeEmits<typeof __VLS_255.emit>;
}
(__VLS_250.slots!).default;
}
(__VLS_245.slots!).default;
}
{
let __VLS_257!: 'VCol' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VCol : (typeof __VLS_resolvedLocalAndGlobalComponents)['VCol'];
const __VLS_258 = __VLS_asFunctionalComponent(__VLS_257, new __VLS_257({ ...{}, cols: ("3"), }));
({} as { VCol: typeof __VLS_257; }).VCol;
({} as { VCol: typeof __VLS_257; }).VCol;
const __VLS_259 = __VLS_258({ ...{}, cols: ("3"), }, ...__VLS_functionalComponentArgsRest(__VLS_258));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_257, typeof __VLS_259> & Record<string, unknown>) => void)({ ...{}, cols: ("3"), });
const __VLS_260 = __VLS_pickFunctionalComponentCtx(__VLS_257, __VLS_259)!;
let __VLS_261!: __VLS_NormalizeEmits<typeof __VLS_260.emit>;
{
let __VLS_262!: 'VBtn' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VBtn : (typeof __VLS_resolvedLocalAndGlobalComponents)['VBtn'];
const __VLS_263 = __VLS_asFunctionalComponent(__VLS_262, new __VLS_262({ ...{ onClick: {} as any, }, color: ("primary"), class: ("px-2 py-2"), outlined: (true), }));
({} as { VBtn: typeof __VLS_262; }).VBtn;
({} as { VBtn: typeof __VLS_262; }).VBtn;
const __VLS_264 = __VLS_263({ ...{ onClick: {} as any, }, color: ("primary"), class: ("px-2 py-2"), outlined: (true), }, ...__VLS_functionalComponentArgsRest(__VLS_263));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_262, typeof __VLS_264> & Record<string, unknown>) => void)({ ...{ onClick: {} as any, }, color: ("primary"), class: ("px-2 py-2"), outlined: (true), });
const __VLS_265 = __VLS_pickFunctionalComponentCtx(__VLS_262, __VLS_264)!;
let __VLS_266!: __VLS_NormalizeEmits<typeof __VLS_265.emit>;
let __VLS_267 = { 'click': __VLS_pickEvent(__VLS_266['click'], ({} as __VLS_FunctionalComponentProps<typeof __VLS_263, typeof __VLS_264>).onClick) };
__VLS_267 = { click: (__VLS_ctx.updateDataIssues) };
if (__VLS_ctx.selectedRows.length > 1) {
{
const __VLS_268 = __VLS_intrinsicElements["span"];
const __VLS_269 = __VLS_elementAsFunctionalComponent(__VLS_268);
const __VLS_270 = __VLS_269({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_269));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_268, typeof __VLS_270> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_271 = __VLS_pickFunctionalComponentCtx(__VLS_268, __VLS_270)!;
let __VLS_272!: __VLS_NormalizeEmits<typeof __VLS_271.emit>;
(__VLS_271.slots!).default;
}
// @ts-ignore
[action, actions, action, actions, action, actions, updateDataIssues, selectedRows,];
}
else {
{
const __VLS_273 = __VLS_intrinsicElements["span"];
const __VLS_274 = __VLS_elementAsFunctionalComponent(__VLS_273);
const __VLS_275 = __VLS_274({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_274));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_273, typeof __VLS_275> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_276 = __VLS_pickFunctionalComponentCtx(__VLS_273, __VLS_275)!;
let __VLS_277!: __VLS_NormalizeEmits<typeof __VLS_276.emit>;
(__VLS_276.slots!).default;
}
}
(__VLS_265.slots!).default;
}
(__VLS_260.slots!).default;
}
(__VLS_240.slots!).default;
}
(__VLS_235.slots!).default;
}
(__VLS_8.slots!).default;
}
{
const __VLS_278 = __VLS_intrinsicElements["div"];
const __VLS_279 = __VLS_elementAsFunctionalComponent(__VLS_278);
const __VLS_280 = __VLS_279({ ...{}, class: ("pagination"), }, ...__VLS_functionalComponentArgsRest(__VLS_279));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_278, typeof __VLS_280> & Record<string, unknown>) => void)({ ...{}, class: ("pagination"), });
const __VLS_281 = __VLS_pickFunctionalComponentCtx(__VLS_278, __VLS_280)!;
let __VLS_282!: __VLS_NormalizeEmits<typeof __VLS_281.emit>;
{
let __VLS_283!: 'VPagination' extends keyof typeof __VLS_ctx ? typeof __VLS_ctx.VPagination : (typeof __VLS_resolvedLocalAndGlobalComponents)['VPagination'];
const __VLS_284 = __VLS_asFunctionalComponent(__VLS_283, new __VLS_283({ ...{ onClick: {} as any, }, modelValue: ((__VLS_ctx.currentPage)), length: ((Math.ceil(__VLS_ctx.totalItems / __VLS_ctx.perPage))), }));
({} as { VPagination: typeof __VLS_283; }).VPagination;
const __VLS_285 = __VLS_284({ ...{ onClick: {} as any, }, modelValue: ((__VLS_ctx.currentPage)), length: ((Math.ceil(__VLS_ctx.totalItems / __VLS_ctx.perPage))), }, ...__VLS_functionalComponentArgsRest(__VLS_284));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_283, typeof __VLS_285> & Record<string, unknown>) => void)({ ...{ onClick: {} as any, }, modelValue: ((__VLS_ctx.currentPage)), length: ((Math.ceil(__VLS_ctx.totalItems / __VLS_ctx.perPage))), });
const __VLS_286 = __VLS_pickFunctionalComponentCtx(__VLS_283, __VLS_285)!;
let __VLS_287!: __VLS_NormalizeEmits<typeof __VLS_286.emit>;
let __VLS_288 = { 'click': __VLS_pickEvent(__VLS_287['click'], ({} as __VLS_FunctionalComponentProps<typeof __VLS_284, typeof __VLS_285>).onClick) };
__VLS_288 = { click: (__VLS_ctx.loadData) };
}
(__VLS_281.slots!).default;
}
(__VLS_3.slots!).default;
}
if (typeof __VLS_styleScopedClasses === 'object' && !Array.isArray(__VLS_styleScopedClasses)) {
__VLS_styleScopedClasses["px-2"];
__VLS_styleScopedClasses["m-0"];
__VLS_styleScopedClasses["select-per-page"];
__VLS_styleScopedClasses["select-per-page"];
__VLS_styleScopedClasses["select-per-page"];
__VLS_styleScopedClasses["text-right"];
__VLS_styleScopedClasses["m-auto"];
__VLS_styleScopedClasses["uil"];
__VLS_styleScopedClasses["uil-search"];
__VLS_styleScopedClasses["text-right"];
__VLS_styleScopedClasses["text-error"];
__VLS_styleScopedClasses["data-issues-table"];
__VLS_styleScopedClasses["text-muted"];
__VLS_styleScopedClasses["px-2"];
__VLS_styleScopedClasses["px-2"];
__VLS_styleScopedClasses["py-2"];
__VLS_styleScopedClasses["select-action"];
__VLS_styleScopedClasses["px-2"];
__VLS_styleScopedClasses["py-2"];
__VLS_styleScopedClasses["pagination"];
}
var __VLS_slots!: {};
// @ts-ignore
[currentPage, totalItems, perPage, currentPage, totalItems, perPage, currentPage, totalItems, perPage, loadData,];
return __VLS_slots;
}
