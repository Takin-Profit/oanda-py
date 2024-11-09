from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_external_user_info_response_200 import GetExternalUserInfoResponse200
from ...types import Response


def _get_kwargs(
    user_specifier: str,
    *,
    authorization: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["Authorization"] = authorization

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/users/{user_specifier}/externalInfo",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetExternalUserInfoResponse200]]:
    if response.status_code == 200:
        response_200 = GetExternalUserInfoResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 405:
        response_405 = cast(Any, None)
        return response_405
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetExternalUserInfoResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_specifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: str,
) -> Response[Union[Any, GetExternalUserInfoResponse200]]:
    """External User Info

     Fetch the externally-available user information for the specified user. This endpoint is intended to
    be used by 3rd parties that have been authorized by a user to view their personal information.

    Args:
        user_specifier (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetExternalUserInfoResponse200]]
    """

    kwargs = _get_kwargs(
        user_specifier=user_specifier,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_specifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: str,
) -> Optional[Union[Any, GetExternalUserInfoResponse200]]:
    """External User Info

     Fetch the externally-available user information for the specified user. This endpoint is intended to
    be used by 3rd parties that have been authorized by a user to view their personal information.

    Args:
        user_specifier (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetExternalUserInfoResponse200]
    """

    return sync_detailed(
        user_specifier=user_specifier,
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    user_specifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: str,
) -> Response[Union[Any, GetExternalUserInfoResponse200]]:
    """External User Info

     Fetch the externally-available user information for the specified user. This endpoint is intended to
    be used by 3rd parties that have been authorized by a user to view their personal information.

    Args:
        user_specifier (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetExternalUserInfoResponse200]]
    """

    kwargs = _get_kwargs(
        user_specifier=user_specifier,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_specifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: str,
) -> Optional[Union[Any, GetExternalUserInfoResponse200]]:
    """External User Info

     Fetch the externally-available user information for the specified user. This endpoint is intended to
    be used by 3rd parties that have been authorized by a user to view their personal information.

    Args:
        user_specifier (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetExternalUserInfoResponse200]
    """

    return (
        await asyncio_detailed(
            user_specifier=user_specifier,
            client=client,
            authorization=authorization,
        )
    ).parsed
