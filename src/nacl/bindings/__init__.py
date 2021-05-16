# Copyright 2013-2019 Donald Stufft and individual contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import, division, print_function

from nacl.bindings.crypto_aead import (
    crypto_aead_chacha20poly1305_ABYTES,
    crypto_aead_chacha20poly1305_KEYBYTES,
    crypto_aead_chacha20poly1305_MESSAGEBYTES_MAX,
    crypto_aead_chacha20poly1305_NPUBBYTES,
    crypto_aead_chacha20poly1305_NSECBYTES,
    crypto_aead_chacha20poly1305_decrypt,
    crypto_aead_chacha20poly1305_encrypt,
    crypto_aead_chacha20poly1305_ietf_ABYTES,
    crypto_aead_chacha20poly1305_ietf_KEYBYTES,
    crypto_aead_chacha20poly1305_ietf_MESSAGEBYTES_MAX,
    crypto_aead_chacha20poly1305_ietf_NPUBBYTES,
    crypto_aead_chacha20poly1305_ietf_NSECBYTES,
    crypto_aead_chacha20poly1305_ietf_decrypt,
    crypto_aead_chacha20poly1305_ietf_encrypt,
    crypto_aead_xchacha20poly1305_ietf_ABYTES,
    crypto_aead_xchacha20poly1305_ietf_KEYBYTES,
    crypto_aead_xchacha20poly1305_ietf_MESSAGEBYTES_MAX,
    crypto_aead_xchacha20poly1305_ietf_NPUBBYTES,
    crypto_aead_xchacha20poly1305_ietf_NSECBYTES,
    crypto_aead_xchacha20poly1305_ietf_decrypt,
    crypto_aead_xchacha20poly1305_ietf_encrypt,
)
from nacl.bindings.crypto_box import (
    crypto_box,
    crypto_box_BEFORENMBYTES,
    crypto_box_BOXZEROBYTES,
    crypto_box_NONCEBYTES,
    crypto_box_PUBLICKEYBYTES,
    crypto_box_SEALBYTES,
    crypto_box_SECRETKEYBYTES,
    crypto_box_SEEDBYTES,
    crypto_box_ZEROBYTES,
    crypto_box_afternm,
    crypto_box_beforenm,
    crypto_box_keypair,
    crypto_box_open,
    crypto_box_open_afternm,
    crypto_box_seal,
    crypto_box_seal_open,
    crypto_box_seed_keypair,
)
from nacl.bindings.crypto_core import (
    crypto_core_ed25519_BYTES,
    crypto_core_ed25519_NONREDUCEDSCALARBYTES,
    crypto_core_ed25519_SCALARBYTES,
    crypto_core_ed25519_add,
    crypto_core_ed25519_is_valid_point,
    crypto_core_ed25519_scalar_add,
    crypto_core_ed25519_scalar_complement,
    crypto_core_ed25519_scalar_invert,
    crypto_core_ed25519_scalar_mul,
    crypto_core_ed25519_scalar_negate,
    crypto_core_ed25519_scalar_reduce,
    crypto_core_ed25519_scalar_sub,
    crypto_core_ed25519_sub,
    has_crypto_core_ed25519,
)
from nacl.bindings.crypto_core_ristretto255 import (
    crypto_core_ristretto255_BYTES,
    crypto_core_ristretto255_GROUP_ORDER,
    crypto_core_ristretto255_HASH_BYTES,
    crypto_core_ristretto255_NONREDUCED_SCALAR_BYTES,
    crypto_core_ristretto255_SCALAR_BYTES,
    crypto_core_ristretto255_add,
    crypto_core_ristretto255_from_hash,
    crypto_core_ristretto255_is_valid_point,
    crypto_core_ristretto255_random,
    crypto_core_ristretto255_scalar_add,
    crypto_core_ristretto255_scalar_complement,
    crypto_core_ristretto255_scalar_invert,
    crypto_core_ristretto255_scalar_mul,
    crypto_core_ristretto255_scalar_negate,
    crypto_core_ristretto255_scalar_random,
    crypto_core_ristretto255_scalar_reduce,
    crypto_core_ristretto255_scalar_sub,
    crypto_core_ristretto255_sub,
    has_crypto_core_ristretto25519,
)
from nacl.bindings.crypto_generichash import (
    crypto_generichash_BYTES,
    crypto_generichash_BYTES_MAX,
    crypto_generichash_BYTES_MIN,
    crypto_generichash_KEYBYTES,
    crypto_generichash_KEYBYTES_MAX,
    crypto_generichash_KEYBYTES_MIN,
    crypto_generichash_PERSONALBYTES,
    crypto_generichash_SALTBYTES,
    crypto_generichash_STATEBYTES,
    generichash_blake2b_final as crypto_generichash_blake2b_final,
    generichash_blake2b_init as crypto_generichash_blake2b_init,
    generichash_blake2b_salt_personal as crypto_generichash_blake2b_salt_personal,
    generichash_blake2b_update as crypto_generichash_blake2b_update,
)
from nacl.bindings.crypto_hash import (
    crypto_hash,
    crypto_hash_BYTES,
    crypto_hash_sha256,
    crypto_hash_sha256_BYTES,
    crypto_hash_sha512,
    crypto_hash_sha512_BYTES,
)
from nacl.bindings.crypto_kx import (
    crypto_kx_PUBLIC_KEY_BYTES,
    crypto_kx_SECRET_KEY_BYTES,
    crypto_kx_SEED_BYTES,
    crypto_kx_SESSION_KEY_BYTES,
    crypto_kx_client_session_keys,
    crypto_kx_keypair,
    crypto_kx_seed_keypair,
    crypto_kx_server_session_keys,
)
from nacl.bindings.crypto_pwhash import (
    crypto_pwhash_ALG_ARGON2I13,
    crypto_pwhash_ALG_ARGON2ID13,
    crypto_pwhash_ALG_DEFAULT,
    crypto_pwhash_BYTES_MAX,
    crypto_pwhash_BYTES_MIN,
    crypto_pwhash_PASSWD_MAX,
    crypto_pwhash_PASSWD_MIN,
    crypto_pwhash_SALTBYTES,
    crypto_pwhash_STRBYTES,
    crypto_pwhash_alg,
    crypto_pwhash_argon2i_MEMLIMIT_INTERACTIVE,
    crypto_pwhash_argon2i_MEMLIMIT_MAX,
    crypto_pwhash_argon2i_MEMLIMIT_MIN,
    crypto_pwhash_argon2i_MEMLIMIT_MODERATE,
    crypto_pwhash_argon2i_MEMLIMIT_SENSITIVE,
    crypto_pwhash_argon2i_OPSLIMIT_INTERACTIVE,
    crypto_pwhash_argon2i_OPSLIMIT_MAX,
    crypto_pwhash_argon2i_OPSLIMIT_MIN,
    crypto_pwhash_argon2i_OPSLIMIT_MODERATE,
    crypto_pwhash_argon2i_OPSLIMIT_SENSITIVE,
    crypto_pwhash_argon2i_STRPREFIX,
    crypto_pwhash_argon2id_MEMLIMIT_INTERACTIVE,
    crypto_pwhash_argon2id_MEMLIMIT_MAX,
    crypto_pwhash_argon2id_MEMLIMIT_MIN,
    crypto_pwhash_argon2id_MEMLIMIT_MODERATE,
    crypto_pwhash_argon2id_MEMLIMIT_SENSITIVE,
    crypto_pwhash_argon2id_OPSLIMIT_INTERACTIVE,
    crypto_pwhash_argon2id_OPSLIMIT_MAX,
    crypto_pwhash_argon2id_OPSLIMIT_MIN,
    crypto_pwhash_argon2id_OPSLIMIT_MODERATE,
    crypto_pwhash_argon2id_OPSLIMIT_SENSITIVE,
    crypto_pwhash_argon2id_STRPREFIX,
    crypto_pwhash_scryptsalsa208sha256_BYTES_MAX,
    crypto_pwhash_scryptsalsa208sha256_BYTES_MIN,
    crypto_pwhash_scryptsalsa208sha256_MEMLIMIT_INTERACTIVE,
    crypto_pwhash_scryptsalsa208sha256_MEMLIMIT_MAX,
    crypto_pwhash_scryptsalsa208sha256_MEMLIMIT_MIN,
    crypto_pwhash_scryptsalsa208sha256_MEMLIMIT_SENSITIVE,
    crypto_pwhash_scryptsalsa208sha256_OPSLIMIT_INTERACTIVE,
    crypto_pwhash_scryptsalsa208sha256_OPSLIMIT_MAX,
    crypto_pwhash_scryptsalsa208sha256_OPSLIMIT_MIN,
    crypto_pwhash_scryptsalsa208sha256_OPSLIMIT_SENSITIVE,
    crypto_pwhash_scryptsalsa208sha256_PASSWD_MAX,
    crypto_pwhash_scryptsalsa208sha256_PASSWD_MIN,
    crypto_pwhash_scryptsalsa208sha256_SALTBYTES,
    crypto_pwhash_scryptsalsa208sha256_STRBYTES,
    crypto_pwhash_scryptsalsa208sha256_STRPREFIX,
    crypto_pwhash_scryptsalsa208sha256_ll,
    crypto_pwhash_scryptsalsa208sha256_str,
    crypto_pwhash_scryptsalsa208sha256_str_verify,
    crypto_pwhash_str_alg,
    crypto_pwhash_str_verify,
    has_crypto_pwhash_scryptsalsa208sha256,
    nacl_bindings_pick_scrypt_params,
)
from nacl.bindings.crypto_scalarmult import (
    crypto_scalarmult,
    crypto_scalarmult_BYTES,
    crypto_scalarmult_SCALARBYTES,
    crypto_scalarmult_base,
    crypto_scalarmult_ed25519,
    crypto_scalarmult_ed25519_BYTES,
    crypto_scalarmult_ed25519_SCALARBYTES,
    crypto_scalarmult_ed25519_base,
    crypto_scalarmult_ed25519_base_noclamp,
    crypto_scalarmult_ed25519_noclamp,
    has_crypto_scalarmult_ed25519,
)
from nacl.bindings.crypto_scalarmult_ristretto255 import (
    crypto_scalarmult_ristretto255,
    crypto_scalarmult_ristretto255_BYTES,
    crypto_scalarmult_ristretto255_SCALAR_BYTES,
    crypto_scalarmult_ristretto255_base,
    has_crypto_scalarmult_ristretto25519,
)
from nacl.bindings.crypto_secretbox import (
    crypto_secretbox,
    crypto_secretbox_BOXZEROBYTES,
    crypto_secretbox_KEYBYTES,
    crypto_secretbox_MACBYTES,
    crypto_secretbox_MESSAGEBYTES_MAX,
    crypto_secretbox_NONCEBYTES,
    crypto_secretbox_ZEROBYTES,
    crypto_secretbox_open,
)
from nacl.bindings.crypto_secretstream import (
    crypto_secretstream_xchacha20poly1305_ABYTES,
    crypto_secretstream_xchacha20poly1305_HEADERBYTES,
    crypto_secretstream_xchacha20poly1305_KEYBYTES,
    crypto_secretstream_xchacha20poly1305_STATEBYTES,
    crypto_secretstream_xchacha20poly1305_TAG_FINAL,
    crypto_secretstream_xchacha20poly1305_TAG_MESSAGE,
    crypto_secretstream_xchacha20poly1305_TAG_PUSH,
    crypto_secretstream_xchacha20poly1305_TAG_REKEY,
    crypto_secretstream_xchacha20poly1305_init_pull,
    crypto_secretstream_xchacha20poly1305_init_push,
    crypto_secretstream_xchacha20poly1305_keygen,
    crypto_secretstream_xchacha20poly1305_pull,
    crypto_secretstream_xchacha20poly1305_push,
    crypto_secretstream_xchacha20poly1305_rekey,
    crypto_secretstream_xchacha20poly1305_state,
)
from nacl.bindings.crypto_shorthash import (
    BYTES as crypto_shorthash_siphash24_BYTES,
    KEYBYTES as crypto_shorthash_siphash24_KEYBYTES,
    XBYTES as crypto_shorthash_siphashx24_BYTES,
    XKEYBYTES as crypto_shorthash_siphashx24_KEYBYTES,
    crypto_shorthash_siphash24,
    crypto_shorthash_siphashx24,
    has_crypto_shorthash_siphashx24,
)
from nacl.bindings.crypto_sign import (
    crypto_sign,
    crypto_sign_BYTES,
    crypto_sign_PUBLICKEYBYTES,
    crypto_sign_SECRETKEYBYTES,
    crypto_sign_SEEDBYTES,
    crypto_sign_ed25519_pk_to_curve25519,
    crypto_sign_ed25519_sk_to_curve25519,
    crypto_sign_ed25519_sk_to_pk,
    crypto_sign_ed25519_sk_to_seed,
    crypto_sign_ed25519ph_STATEBYTES,
    crypto_sign_ed25519ph_final_create,
    crypto_sign_ed25519ph_final_verify,
    crypto_sign_ed25519ph_state,
    crypto_sign_ed25519ph_update,
    crypto_sign_keypair,
    crypto_sign_open,
    crypto_sign_seed_keypair,
)
from nacl.bindings.randombytes import (
    randombytes,
    randombytes_buf_deterministic,
)
from nacl.bindings.sodium_core import sodium_init
from nacl.bindings.utils import (
    sodium_add,
    sodium_increment,
    sodium_is_zero,
    sodium_memcmp,
    sodium_pad,
    sodium_unpad,
)


__all__ = [
    "crypto_aead_chacha20poly1305_ABYTES",
    "crypto_aead_chacha20poly1305_KEYBYTES",
    "crypto_aead_chacha20poly1305_MESSAGEBYTES_MAX",
    "crypto_aead_chacha20poly1305_NPUBBYTES",
    "crypto_aead_chacha20poly1305_NSECBYTES",
    "crypto_aead_chacha20poly1305_decrypt",
    "crypto_aead_chacha20poly1305_encrypt",
    "crypto_aead_chacha20poly1305_ietf_ABYTES",
    "crypto_aead_chacha20poly1305_ietf_KEYBYTES",
    "crypto_aead_chacha20poly1305_ietf_MESSAGEBYTES_MAX",
    "crypto_aead_chacha20poly1305_ietf_NPUBBYTES",
    "crypto_aead_chacha20poly1305_ietf_NSECBYTES",
    "crypto_aead_chacha20poly1305_ietf_decrypt",
    "crypto_aead_chacha20poly1305_ietf_encrypt",
    "crypto_aead_xchacha20poly1305_ietf_ABYTES",
    "crypto_aead_xchacha20poly1305_ietf_KEYBYTES",
    "crypto_aead_xchacha20poly1305_ietf_MESSAGEBYTES_MAX",
    "crypto_aead_xchacha20poly1305_ietf_NPUBBYTES",
    "crypto_aead_xchacha20poly1305_ietf_NSECBYTES",
    "crypto_aead_xchacha20poly1305_ietf_decrypt",
    "crypto_aead_xchacha20poly1305_ietf_encrypt",
    "crypto_box_SECRETKEYBYTES",
    "crypto_box_PUBLICKEYBYTES",
    "crypto_box_SEEDBYTES",
    "crypto_box_NONCEBYTES",
    "crypto_box_ZEROBYTES",
    "crypto_box_BOXZEROBYTES",
    "crypto_box_BEFORENMBYTES",
    "crypto_box_SEALBYTES",
    "crypto_box_keypair",
    "crypto_box",
    "crypto_box_open",
    "crypto_box_beforenm",
    "crypto_box_afternm",
    "crypto_box_open_afternm",
    "crypto_box_seal",
    "crypto_box_seal_open",
    "crypto_box_seed_keypair",
    "has_crypto_core_ed25519",
    "crypto_core_ed25519_BYTES",
    "crypto_core_ed25519_SCALARBYTES",
    "crypto_core_ed25519_NONREDUCEDSCALARBYTES",
    "crypto_core_ed25519_add",
    "crypto_core_ed25519_is_valid_point",
    "crypto_core_ed25519_sub",
    "crypto_core_ed25519_scalar_invert",
    "crypto_core_ed25519_scalar_negate",
    "crypto_core_ed25519_scalar_complement",
    "crypto_core_ed25519_scalar_add",
    "crypto_core_ed25519_scalar_sub",
    "crypto_core_ed25519_scalar_mul",
    "crypto_core_ed25519_scalar_reduce",
    "has_crypto_core_ristretto25519",
    "crypto_core_ristretto255_SCALAR_BYTES",
    "crypto_core_ristretto255_NONREDUCED_SCALAR_BYTES",
    "crypto_core_ristretto255_GROUP_ORDER",
    "crypto_core_ristretto255_scalar_add",
    "crypto_core_ristretto255_scalar_complement",
    "crypto_core_ristretto255_scalar_invert",
    "crypto_core_ristretto255_scalar_mul",
    "crypto_core_ristretto255_scalar_negate",
    "crypto_core_ristretto255_scalar_random",
    "crypto_core_ristretto255_scalar_reduce",
    "crypto_core_ristretto255_scalar_sub",
    "crypto_core_ristretto255_BYTES",
    "crypto_core_ristretto255_HASH_BYTES",
    "crypto_core_ristretto255_add",
    "crypto_core_ristretto255_from_hash",
    "crypto_core_ristretto255_is_valid_point",
    "crypto_core_ristretto255_sub",
    "crypto_core_ristretto255_random",
    "crypto_hash_BYTES",
    "crypto_hash_sha256_BYTES",
    "crypto_hash_sha512_BYTES",
    "crypto_hash",
    "crypto_hash_sha256",
    "crypto_hash_sha512",
    "crypto_generichash_BYTES",
    "crypto_generichash_BYTES_MIN",
    "crypto_generichash_BYTES_MAX",
    "crypto_generichash_KEYBYTES",
    "crypto_generichash_KEYBYTES_MIN",
    "crypto_generichash_KEYBYTES_MAX",
    "crypto_generichash_SALTBYTES",
    "crypto_generichash_PERSONALBYTES",
    "crypto_generichash_STATEBYTES",
    "crypto_generichash_blake2b_salt_personal",
    "crypto_generichash_blake2b_init",
    "crypto_generichash_blake2b_update",
    "crypto_generichash_blake2b_final",
    "crypto_kx_keypair",
    "crypto_kx_seed_keypair",
    "crypto_kx_client_session_keys",
    "crypto_kx_server_session_keys",
    "crypto_kx_PUBLIC_KEY_BYTES",
    "crypto_kx_SECRET_KEY_BYTES",
    "crypto_kx_SEED_BYTES",
    "crypto_kx_SESSION_KEY_BYTES",
    "has_crypto_scalarmult_ed25519",
    "crypto_scalarmult_BYTES",
    "crypto_scalarmult_SCALARBYTES",
    "crypto_scalarmult",
    "crypto_scalarmult_base",
    "crypto_scalarmult_ed25519_BYTES",
    "crypto_scalarmult_ed25519_SCALARBYTES",
    "crypto_scalarmult_ed25519",
    "crypto_scalarmult_ed25519_base",
    "crypto_scalarmult_ed25519_noclamp",
    "crypto_scalarmult_ed25519_base_noclamp",
    "has_crypto_scalarmult_ristretto25519",
    "crypto_scalarmult_ristretto255_BYTES",
    "crypto_scalarmult_ristretto255_SCALAR_BYTES",
    "crypto_scalarmult_ristretto255_base",
    "crypto_scalarmult_ristretto255",
    "crypto_secretbox_KEYBYTES",
    "crypto_secretbox_NONCEBYTES",
    "crypto_secretbox_ZEROBYTES",
    "crypto_secretbox_BOXZEROBYTES",
    "crypto_secretbox_MACBYTES",
    "crypto_secretbox_MESSAGEBYTES_MAX",
    "crypto_secretbox",
    "crypto_secretbox_open",
    "crypto_secretstream_xchacha20poly1305_ABYTES",
    "crypto_secretstream_xchacha20poly1305_HEADERBYTES",
    "crypto_secretstream_xchacha20poly1305_KEYBYTES",
    "crypto_secretstream_xchacha20poly1305_STATEBYTES",
    "crypto_secretstream_xchacha20poly1305_TAG_FINAL",
    "crypto_secretstream_xchacha20poly1305_TAG_MESSAGE",
    "crypto_secretstream_xchacha20poly1305_TAG_PUSH",
    "crypto_secretstream_xchacha20poly1305_TAG_REKEY",
    "crypto_secretstream_xchacha20poly1305_init_pull",
    "crypto_secretstream_xchacha20poly1305_init_push",
    "crypto_secretstream_xchacha20poly1305_keygen",
    "crypto_secretstream_xchacha20poly1305_pull",
    "crypto_secretstream_xchacha20poly1305_push",
    "crypto_secretstream_xchacha20poly1305_rekey",
    "crypto_secretstream_xchacha20poly1305_state",
    "has_crypto_shorthash_siphashx24",
    "crypto_shorthash_siphash24_BYTES",
    "crypto_shorthash_siphash24_KEYBYTES",
    "crypto_shorthash_siphash24",
    "crypto_shorthash_siphashx24_BYTES",
    "crypto_shorthash_siphashx24_KEYBYTES",
    "crypto_shorthash_siphashx24",
    "crypto_sign_BYTES",
    "crypto_sign_SEEDBYTES",
    "crypto_sign_PUBLICKEYBYTES",
    "crypto_sign_SECRETKEYBYTES",
    "crypto_sign_keypair",
    "crypto_sign_seed_keypair",
    "crypto_sign",
    "crypto_sign_open",
    "crypto_sign_ed25519_pk_to_curve25519",
    "crypto_sign_ed25519_sk_to_curve25519",
    "crypto_sign_ed25519_sk_to_pk",
    "crypto_sign_ed25519_sk_to_seed",
    "crypto_sign_ed25519ph_STATEBYTES",
    "crypto_sign_ed25519ph_final_create",
    "crypto_sign_ed25519ph_final_verify",
    "crypto_sign_ed25519ph_state",
    "crypto_sign_ed25519ph_update",
    "crypto_pwhash_ALG_ARGON2I13",
    "crypto_pwhash_ALG_ARGON2ID13",
    "crypto_pwhash_ALG_DEFAULT",
    "crypto_pwhash_BYTES_MAX",
    "crypto_pwhash_BYTES_MIN",
    "crypto_pwhash_PASSWD_MAX",
    "crypto_pwhash_PASSWD_MIN",
    "crypto_pwhash_SALTBYTES",
    "crypto_pwhash_STRBYTES",
    "crypto_pwhash_alg",
    "crypto_pwhash_argon2i_MEMLIMIT_MIN",
    "crypto_pwhash_argon2i_MEMLIMIT_MAX",
    "crypto_pwhash_argon2i_MEMLIMIT_INTERACTIVE",
    "crypto_pwhash_argon2i_MEMLIMIT_MODERATE",
    "crypto_pwhash_argon2i_MEMLIMIT_SENSITIVE",
    "crypto_pwhash_argon2i_OPSLIMIT_MIN",
    "crypto_pwhash_argon2i_OPSLIMIT_MAX",
    "crypto_pwhash_argon2i_OPSLIMIT_INTERACTIVE",
    "crypto_pwhash_argon2i_OPSLIMIT_MODERATE",
    "crypto_pwhash_argon2i_OPSLIMIT_SENSITIVE",
    "crypto_pwhash_argon2i_STRPREFIX",
    "crypto_pwhash_argon2id_MEMLIMIT_MIN",
    "crypto_pwhash_argon2id_MEMLIMIT_MAX",
    "crypto_pwhash_argon2id_MEMLIMIT_INTERACTIVE",
    "crypto_pwhash_argon2id_MEMLIMIT_MODERATE",
    "crypto_pwhash_argon2id_OPSLIMIT_MIN",
    "crypto_pwhash_argon2id_OPSLIMIT_MAX",
    "crypto_pwhash_argon2id_MEMLIMIT_SENSITIVE",
    "crypto_pwhash_argon2id_OPSLIMIT_INTERACTIVE",
    "crypto_pwhash_argon2id_OPSLIMIT_MODERATE",
    "crypto_pwhash_argon2id_OPSLIMIT_SENSITIVE",
    "crypto_pwhash_argon2id_STRPREFIX",
    "crypto_pwhash_str_alg",
    "crypto_pwhash_str_verify",
    "has_crypto_pwhash_scryptsalsa208sha256",
    "crypto_pwhash_scryptsalsa208sha256_BYTES_MAX",
    "crypto_pwhash_scryptsalsa208sha256_BYTES_MIN",
    "crypto_pwhash_scryptsalsa208sha256_MEMLIMIT_INTERACTIVE",
    "crypto_pwhash_scryptsalsa208sha256_MEMLIMIT_MAX",
    "crypto_pwhash_scryptsalsa208sha256_MEMLIMIT_MIN",
    "crypto_pwhash_scryptsalsa208sha256_MEMLIMIT_SENSITIVE",
    "crypto_pwhash_scryptsalsa208sha256_OPSLIMIT_INTERACTIVE",
    "crypto_pwhash_scryptsalsa208sha256_OPSLIMIT_MAX",
    "crypto_pwhash_scryptsalsa208sha256_OPSLIMIT_MIN",
    "crypto_pwhash_scryptsalsa208sha256_OPSLIMIT_SENSITIVE",
    "crypto_pwhash_scryptsalsa208sha256_PASSWD_MAX",
    "crypto_pwhash_scryptsalsa208sha256_PASSWD_MIN",
    "crypto_pwhash_scryptsalsa208sha256_SALTBYTES",
    "crypto_pwhash_scryptsalsa208sha256_STRBYTES",
    "crypto_pwhash_scryptsalsa208sha256_STRPREFIX",
    "crypto_pwhash_scryptsalsa208sha256_ll",
    "crypto_pwhash_scryptsalsa208sha256_str",
    "crypto_pwhash_scryptsalsa208sha256_str_verify",
    "nacl_bindings_pick_scrypt_params",
    "randombytes",
    "randombytes_buf_deterministic",
    "sodium_init",
    "sodium_add",
    "sodium_increment",
    "sodium_is_zero",
    "sodium_memcmp",
    "sodium_pad",
    "sodium_unpad",
]


# Initialize Sodium
sodium_init()
