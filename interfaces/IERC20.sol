// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0;

interface IERC20 {
    function transfer(address to, uint256 value) external;

    function transferFrom(
        address from,
        address to,
        uint256 value
    ) external;

    function balanceOf(address tokenOwner) external returns (uint256 balance);
}
