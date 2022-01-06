// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0;

import "../interfaces/IERC20.sol";

contract BulkSender {
    function bulksendToken(
        IERC20 _token,
        address[] memory _to,
        uint256[] memory _values
    ) public {
        require(_to.length == _values.length);
        for (uint256 i = 0; i < _to.length; i++) {
            _token.transferFrom(msg.sender, _to[i], _values[i]);
        }
    }
}
