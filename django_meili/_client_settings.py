from typing import Literal, TypedDict


class MinWordSizeForTypos(TypedDict, total=False):
    oneTypo: int
    twoTypos: int


class TypoToleranceSettings(TypedDict, total=False):
    enabled: bool
    minWordSizeForTypos: MinWordSizeForTypos
    disableOnWords: list[str]
    disableOnAttributes: list[str]
    disableOnNumbers: bool


class PaginationSettings(TypedDict, total=False):
    maxTotalHits: int


class FacetingSettings(TypedDict, total=False):
    maxValuesPerFacet: int
    sortFacetValuesBy: dict[str, Literal["alpha", "count"]]


class EmbedderSettings(TypedDict, total=False):
    source: str
    model: str
    apiKey: str
    documentTemplate: str
    documentTemplateMaxBytes: int


class LocalizedAttribute(TypedDict):
    attributePatterns: list[str]
    locales: list[str]


class ChatSearchParameters(TypedDict, total=False):
    limit: int


class ChatSettings(TypedDict, total=False):
    description: str
    documentTemplateMaxBytes: int
    searchParameters: ChatSearchParameters


# --- Principal ---


class MeiliIndexSettings(TypedDict, total=False):
    rankingRules: list[str]

    distinctAttribute: str | None

    searchableAttributes: list[str]
    displayedAttributes: list[str]

    stopWords: list[str]
    synonyms: dict[str, list[str]]

    filterableAttributes: list[str]
    sortableAttributes: list[str]

    typoTolerance: TypoToleranceSettings
    pagination: PaginationSettings
    faceting: FacetingSettings

    dictionary: list[str]

    separatorTokens: list[str]
    nonSeparatorTokens: list[str]

    embedders: dict[str, EmbedderSettings]

    searchCutoffMs: int | None
    proximityPrecision: Literal["byWord", "byAttribute"]

    localizedAttributes: list[LocalizedAttribute]

    facetSearch: bool
    prefixSearch: Literal["indexingTime", "disabled"]

    chat: ChatSettings
