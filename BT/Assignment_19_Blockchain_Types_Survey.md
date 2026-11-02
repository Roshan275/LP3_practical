# Survey Report: Types of Blockchains and Their Real-World Use Cases

**Assignment:** BT Practical 19<br>
**Student:** ____________________<br>
**Roll No.:** ____________________<br>
**Class:** ____________________<br>
**Date:** ____________________

## Abstract

Blockchain networks are commonly described as public, private, consortium, or hybrid. These labels mainly describe who may participate, who governs the network, and how data is shared. This report compares the four models and examines documented examples: Ethereum as a public network; a permissioned supply-chain ledger as a private-network example; Project Jura as a multi-party financial DLT experiment; and Project Acacia as a public-private design. Each model offers different trade-offs in openness, privacy, governance, and performance. The examples also show that a project can be a pilot rather than an operational production service, and that blockchain is useful only when its shared-record and multi-party properties address a real coordination problem.

## 1. Introduction

A blockchain is a shared record maintained by multiple computers or organizations. Participants use agreed rules to propose, validate, and record updates. Once accepted, earlier records are difficult to alter without the network detecting the change. Depending on the design, participants may be anonymous or known, and the records may be broadly visible or restricted.

The four categories in this report are useful shorthand, but they are not four entirely separate technologies. **Public/private** describes access and visibility, while **consortium** describes shared governance by a group of organizations. **Hybrid** describes a design that combines public and restricted components or data. A network could therefore have consortium governance and still connect to a public ledger. The Government of India's National Informatics Centre describes public, private, consortium, and hybrid models using these distinctions in its [blockchain types overview](https://www.blockchain.gov.in/Home/BlockChain?blockchain=type).

## 2. Comparison

| Type | Participation and governance | Typical strengths | Main limitations | Illustrative use |
|---|---|---|---|---|
| Public | Anyone may use the network under its public protocol; validation follows the network's consensus rules. | Open access, broad verifiability, and no single company controlling access. | Public data is difficult to keep confidential; throughput, fees, and governance depend on network design. | Open smart contracts, public tokens, and decentralized applications. |
| Private | One organization or a single operator controls membership and permissions. | Fine-grained access controls, known participants, and governance aligned to one organization. | The operator is a central trust point; fewer independent validators can reduce decentralization. | Internal record sharing or a controlled enterprise workflow. |
| Consortium | A defined set of organizations jointly operate or govern the network. | Shared records between known parties without assigning all control to one member. | Members must agree on rules, access, upgrades, and dispute handling; coordination can be difficult. | Inter-bank settlement experiments or shared industry records. |
| Hybrid | Restricted components handle confidential activity while selected records, proofs, or tokens connect to a public network. | Can combine controlled privacy with public verifiability or interoperability. | More components mean more integration, security, and governance complexity. | Regulated asset settlement that connects private money or records to public infrastructure. |

## 3. Public blockchain

A **public blockchain** is open for public participation. Ethereum describes its base layer as permissionless: users can deploy contracts, call them, run nodes, and build applications under common protocol rules. Its documentation explains Ethereum's public, decentralized execution model in [Why build on Ethereum](https://ethereum.org/latest/why-build-on-ethereum/) and the [technical introduction](https://ethereum.org/developers/docs/intro-to-ethereum/).

### Use case: open smart-contract applications

Ethereum supports applications whose smart-contract rules can be inspected and called by any address. Examples include token contracts and decentralized finance applications that exchange or manage digital assets. A public ledger allows independent users and software to verify contract state without obtaining membership from a private network operator.

### Benefits and limitations

Public networks provide broad access and shared verification. They can make applications composable, because one contract may interact with other public contracts. At the same time, transaction activity and contract state can be visible to the public. Applications may also rely on wallets, interfaces, and RPC providers that add their own availability or censorship risks. Public visibility does not mean that a person's real-world identity is automatically known, but transaction patterns can still reveal information.

## 4. Private blockchain

A **private blockchain** restricts participation. An organization or designated administrator grants identities and assigns permissions. Hyperledger Fabric is a permissioned ledger framework: organizations operate identified peers, and channels can limit which members share particular ledgers. See the [Fabric network documentation](https://hyperledger-fabric.readthedocs.io/en/latest/network/network.html) and [membership documentation](https://hyperledger-fabric.readthedocs.io/en/latest/membership/membership.html).

### Use case: food supply-chain traceability

Hyperledger's 2019 annual report documented Walmart's use of a system powered by Hyperledger Fabric to trace food origins across suppliers. It reported traceability for more than 25 products from five suppliers at that time. The purpose was to make origin information easier to follow across participating supply-chain organizations. This is a **historically documented deployment example**, rather than a claim about the system's current scope; see the [Hyperledger 2019 annual report](https://www.hyperledger.org/hubfs/Hyperledger/Printables/HL_AnnualReport_Print.pdf).

### Benefits and limitations

Known identities and configurable access make permissioned systems suitable when participants cannot publish all business records publicly. A shared ledger can reduce inconsistent copies of records between departments or companies. However, the organization controlling membership and infrastructure remains an important trust point. If the participants already trust one database operator and do not need shared validation, a conventional database may be simpler and less costly.

## 5. Consortium blockchain

A **consortium blockchain** is operated or governed by multiple organizations rather than a single organization. Participants are generally known and admitted under agreed rules. Governance must define who can join, validate transactions, update software, resolve disputes, and recover from operational failures.

### Use case: Project Jura's cross-border settlement experiment

Project Jura was a BIS Innovation Hub experiment involving the Banque de France, Swiss National Bank, and a private-sector consortium. It explored transfers of tokenized euro and Swiss franc central-bank reserves between commercial banks on a DLT platform, including delivery-versus-payment and payment-versus-payment settlement. The BIS describes it as a concluded project in its [Project Jura overview](https://www.bis.org/project/jura).

This is a consortium-style **experimental DLT** example: institutions collaborated around a shared financial process and tested the design. It should not be represented as a currently operating commercial blockchain service. The example demonstrates why multiple regulated institutions may want shared rules while keeping participation controlled.

### Benefits and limitations

Consortium governance distributes decision-making across members and can make known-party processes easier to coordinate. It may offer greater privacy and predictable participation than an open network. Its success depends on governance: members need clear agreements on membership, costs, standards, liability, and upgrades. A consortium is not automatically decentralized; a few powerful members may still dominate decisions.

## 6. Hybrid blockchain

A **hybrid blockchain** combines restricted and public components. Confidential business or regulated activity may remain on a permissioned network, while selected data, proofs, or token representations are exposed or settled through a public network. The two layers must be connected carefully so that the public representation corresponds to the restricted record.

### Use case: Australia's Project Acacia

Project Acacia, led by the Reserve Bank of Australia and the Digital Finance Cooperative Research Centre with industry participants and regulators, explored wholesale tokenized-asset markets. In one pilot, Australian Payments Plus used a public network for a token interchange while the underlying pilot wholesale central-bank digital currency remained on a private network. The final report identifies a public-permissioned Hedera network and private-permissioned Hedera HashSphere network for that use case. See the [RBA and DFCRC Project Acacia announcement](https://www.rba.gov.au/media-releases/2026/mr-26-13.html) and the [Project Acacia final report](https://www.rba.gov.au/payments-and-infrastructure/central-bank-digital-currency/pdf/project-acacia-final-report.pdf).

This example illustrates a public-private architecture rather than a general-purpose consumer blockchain. The project was research and piloting, and the RBA's report describes further work needed before broader adoption. It shows how an institution may seek public-network connectivity while keeping the underlying regulated money under private control.

### Benefits and limitations

Hybrid designs can separate data by sensitivity and allow selected public verification or interoperability. They can be useful when neither a fully public nor a fully private design meets all requirements. The trade-off is added complexity: operators must secure bridges or interchange logic, reconcile records across networks, and clearly define which network is authoritative if an inconsistency occurs.

## 7. Discussion

The models differ most in who is trusted and who can participate. Public networks minimize dependence on a central membership authority, but they can expose transaction data. Private networks provide direct administrative control but concentrate trust. Consortium networks share administration among selected organizations, which requires governance agreements. Hybrid systems combine components and can support privacy plus public verification, but introduce cross-network dependencies.

The examples also show why project status matters when describing “real-world use cases.” A documented production deployment, an historical system, and a proof-of-concept are different kinds of evidence. Project Jura and Project Acacia are useful case studies, but they should be described as experiments or pilots where the source does so. A blockchain should be selected only when several parties need a shared, auditable record and the chosen trust and privacy model is appropriate. It does not automatically improve data quality: inaccurate information entered by a participant can still be recorded immutably.

## 8. Conclusion

Public, private, consortium, and hybrid blockchains are different design choices for participation, governance, and data visibility. Public systems suit open access and independent verification. Private systems offer one organization controlled membership. Consortium systems allow a group of known organizations to share operation and governance. Hybrid systems connect restricted activity with selected public functionality. The appropriate choice depends on the parties involved, confidentiality requirements, governance capacity, and the problem being solved. In some cases, a conventional shared database will be simpler; blockchain is most relevant when independent participants need a common record and shared validation.

## References

1. National Informatics Centre, Government of India, [Types of Blockchain](https://www.blockchain.gov.in/Home/BlockChain?blockchain=type), accessed 2 November 2026.
2. Ethereum.org, [Why build on Ethereum?](https://ethereum.org/latest/why-build-on-ethereum/), accessed 2 November 2026.
3. Ethereum.org, [Technical introduction to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/), accessed 2 November 2026.
4. Hyperledger Fabric, [How Fabric networks are structured](https://hyperledger-fabric.readthedocs.io/en/latest/network/network.html), accessed 2 November 2026.
5. Hyperledger Fabric, [Membership Service Provider](https://hyperledger-fabric.readthedocs.io/en/latest/membership/membership.html), accessed 2 November 2026.
6. Hyperledger, [2019 Annual Report](https://www.hyperledger.org/hubfs/Hyperledger/Printables/HL_AnnualReport_Print.pdf), accessed 2 November 2026.
7. Bank for International Settlements, [Project Jura](https://www.bis.org/project/jura), accessed 2 November 2026.
8. Reserve Bank of Australia and DFCRC, [Project Acacia media release](https://www.rba.gov.au/media-releases/2026/mr-26-13.html), 18 May 2026.
9. Reserve Bank of Australia and DFCRC, [Project Acacia final report](https://www.rba.gov.au/payments-and-infrastructure/central-bank-digital-currency/pdf/project-acacia-final-report.pdf), May 2026.
